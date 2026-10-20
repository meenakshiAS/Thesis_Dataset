def write_error(*args, **kwargs):
    """Redirectable wrapper for print sys.stderr statements."""
    if _logger:
        kwargs.pop("end", None)
        kwargs.pop("file", None)
        _logger.error(*args, **kwargs)
    else:
        print(*args, file=sys.stderr, **kwargs)
