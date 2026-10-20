def xmltreefromfile(filename):
    """Internal function to read an XML file."""
    try:
        return ElementTree.parse(
            filename,
            ElementTree.XMLParser(collect_ids=False)
        )
    except TypeError:
        return ElementTree.parse(
            filename,
            ElementTree.XMLParser()
        )
