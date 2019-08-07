def letters(string: str) -> dict:
    """ Creating a dictionary with counts of letters"""
    set(string)
    letters_dict = {}
    for letter in string:
        letters_dict[letter] = string.count(letter)
    return letters_dict


print(letters('asdfasdfasdfffdssss'))
