def string_validator(name):
    """
    Return True if all characters in name are alpha or white space.
    """

    # strip off any leading/trailing white spaces
    name = name.strip()
    if len(name) < 1:
        return False
    return not len([i for i in name if not (i.isalpha() or i.isspace())])


