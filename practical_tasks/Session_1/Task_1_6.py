def longest_word(text: str):
    """ Looking for the longest word """
    return max(text.split(' '), key=len)


print(longest_word(input('Please, enter your text: ')))