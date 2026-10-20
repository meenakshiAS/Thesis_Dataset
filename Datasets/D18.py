async def storage(dev: Device):
    """Print storage information."""
    storages = await dev.get_storage_list()

    for storage in storages:
        click.echo(storage)
