def read_config_file(path):
    """Returns the configuration from the specified file."""
    try:
        with open(path, 'r') as f:
            return json.load(f, object_pairs_hook=OrderedDict)
    except IOError as ex:
        if ex != errno.ENOENT:
            raise
        return {}