def sum_py(x, y):
    """ sum x and y
    >>> sum_py(10, 20)
    30

    >>> sum_py('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be int or float
    """
    assert isinstance(x, (int, float)), 'x needs to be int or float'
    assert isinstance(y, (int, float)), 'y needs to be int or float'
    return x + y


def sub_py(x, y):
    """sub x and y
    >>> sub_py(10, 5)
    5

    >>> sub_py('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x needs to be int or float
    """
    assert isinstance(x, (int, float)), 'x needs to be int or float'
    assert isinstance(y, (int, float)), 'y needs to be int or float'
    return x - y


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
