def split(text: str, r: str, n: int) -> list:
    """ Splitting of the input string """
    temp = []
    result = []
    text_list = list(text)
    for x in text_list:
        if n != 0:
            if x != r:
                temp.append(x)
            else:
                result.append(temp)
                temp = []
                n -= 1
        elif x != r:
            temp.append(x)
    result.append(temp)
    return result


print(split('1,2,3', ',', 2))