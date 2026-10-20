def read(self, offset, length, min_length=0, unbuffered=False, wait=True, send=True):
    """
    Reads from an opened file or pipe.

    Supports out of band send function, call this function with send=False
    to return a tuple of (SMB2ReadRequest, receive_func) instead of sending
    the request and waiting for the response. The receive_func can be used
    to get the response from the server by passing in the Request that was
    used to sent it out of band.

    :param offset: The offset to start the read of the file.
    :param length: The number of bytes to read from the offset.
    :param min_length: The minimum number of bytes to be read for a successful operation.
    :param unbuffered: Whether the server should cache the read data at intermediate layers,
                       only value for SMB 3.0.2 or newer.
    :param wait: If send=True, whether to wait for a response if STATUS_PENDING was received
                 from the server or fail.
    :param send: Whether to send the request in the same call or return the message to the
                 caller and the unpack function.
    :return: A byte string of the bytes read.
    """
    if length > self.connection.max_read_size:
        raise SMBException(
            "The requested read length %d is greater than "
            "the maximum negotiated read size %d"
            % (length, self.connection.max_read_size)
        )

    read = SMB2ReadRequest()
    read['length'] = length
    read['offset'] = offset
    read['minimum_count'] = min_length
    read['file_id'] = self.file_id
    read['padding'] = b"\x50"

    if unbuffered:
        if self.connection.dialect < Dialects.SMB_3_0_2:
            raise SMBUnsupportedFeature(
                self.connection.dialect,
                Dialects.SMB_3_0_2,
                "SMB2_READFLAG_READ_UNBUFFERED",
                True
            )
        read['flags'].set_flag(ReadFlags.SMB2_READFLAG_READ_UNBUFFERED)

    if not send:
        return read, self._read_response

    log.info(
        "Session: %s, Tree Connect ID: %s - sending SMB2 Read "
        "Request for file %s"
        % (
            self.tree_connect.session.username,
            self.tree_connect.share_name,
            self.file_name
        )
    )
    log.debug(str(read))

    request = self.connection.send(
        read,
        self.tree_connect.session.session_id,
        self.tree_connect.tree_connect_id
    )

    return self._read_response(request, wait)