"""
1 - receive an integer
2 - find out if the number is a multiple of 3 and 5:
    return bacon with eggs
3 - find out if the number is a multiple of only 3:
    return bacon
4 - find out if the number is a multiple of only 5:
    return eggs
5 - find out if the number is not a multiple of 3 and 5:
    return get hungry
"""


def bacon_with_eggs(n):
    assert isinstance(n, int), 'n must be int'

    if n % 3 == 0 and n % 5 == 0:
        return 'bacon with eggs'

    if n % 3 == 0:
        return 'bacon'

    if n % 5 == 0:
        return 'eggs'

    return 'get hungry'
