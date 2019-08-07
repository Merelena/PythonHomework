import string


def test_1(*args) -> set:
    """ Characters that appear in all strings """
    result = set(args[0])
    for item in args[1:]:
        result.intersection_update(set(item))
    return result if args else None


def test_2(*args) -> set:
    """ Characters that appear in at least one string"""
    return set().union(*args) if args else None


def test_3(*args) -> set:
    """ Characters that appear at least in two strings """
    characters = test_2(*args)
    result = set()
    k = 0
    for letter in characters:
        for word in args:
            if letter in word:
                k += 1
        if k >= 2:
            result.add(letter)
            k = 0
    return result


def test_4(*args) -> set:
    """ Characters of alphabet, that were not used in any string """
    characters = set(string.ascii_lowercase)
    for item in args:
        characters -= set(item)
    return characters


print(
    test_1('afd', 'sdf', 'dfg', 'gfd'),
    test_2('afd', 'sdf', 'dfg', 'gfd'),
    test_3('afd', 'sdf', 'dfg', 'gfd'),
    test_4('afd', 'sdf', 'dfg', 'gfd'),
)