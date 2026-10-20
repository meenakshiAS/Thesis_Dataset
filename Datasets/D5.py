def get(self, path, payload=None, headers=None):
    """HTTP GET operation.
    :param path: URI Path
    :param payload: HTTP Body
    :param headers: HTTP Headers
    :raises ApiError: Raises if the remote server encountered an error.
    :raises ApiConnectionError: Raises if there was a connectivity issue.
    :return: Response
    """
    return self._request('get', path, payload, headers)