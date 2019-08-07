def pairs(words: list):
    """ Creating pairs of words """
    result = []
    length = len(words)
    for index, item in enumerate(words):
        if index != length - 1:
            temp_tuple = item, words[index+1]
            result.append(temp_tuple)
    if result:
        return result
    else: return 'None'


print(pairs(['e', 'ye', 't']))