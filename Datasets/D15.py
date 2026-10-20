def get_db(db_name=None):
    """
    GetDB - simple function to wrap getting a database connection
    from the connection pool.
    """
    import pymongo

    return pymongo.Connection(
        host=DB_HOST,
        port=DB_PORT
    )[db_name]
