def get_var(name, factory=None):
    """Gets a global variable given its name.

    If factory is not None and the variable is not set, factory
    is a callable that will set the variable.

    If not set, returns None.
    """
    if name not in _VARS and factory is not None:
        _VARS[name] = factory()
    return _VARS.get(name)