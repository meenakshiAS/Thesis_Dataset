def uuid(anon, obj, field, val):
    """
    Returns a random uuid string
    """

    return anon.faker.uuid(field=field)
