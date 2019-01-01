import six

# Six is a Python2 and Python3 compatibility library

def bytes_to_str(s, encoding='utf-8'):
    """Returns a str if a bytes object is given."""

    if six.PY3 and isinstance(s, bytes):
        return s.decode(encoding)
    return s