def split_by_index(text: str, split_list: list) -> list:
    """ Split by indexes """
    result = []
    temp = ''
    for index, item in enumerate(text):
        temp += text[index-1:index]
        if index in split_list:
            result.append(temp)
            temp = ''
    result.append(temp + text[len(text)-1])
    return result



print(split_by_index('okbyemy', [2, 5]))