def add_plugin(plugin, directory=None):
    """Adds the specified plugin. 
    This returns False if it was already added."""
    repo = require_repo(directory)
    plugins = get_value(repo, 'plugins', expect_type=dict)
    if plugin in plugins:
        return False
    plugins[plugin] = {}
    set_value(repo, 'plugins', plugins)
    return True