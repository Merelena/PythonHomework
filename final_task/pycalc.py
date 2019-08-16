from re import split, findall, sub


def pycalc(string: str):
    """Main function of calculator"""
    brackets_list = findall('[(-)]', string)  # Searching for brackets to check a balance of them
    if brackets_list.count('(') != brackets_list.count(')'):
        raise Exception('ERROR: brackets are not balanced')
    string = merging_pluses_and_minuses(string)
    temp_list = sub('log\w{2}|log\w{1}|log\w{1}\d{1}|atan\w{2}', '', string)  # Helps to extract numbers from 'string'
    numbers_list = findall('[0-9]+', temp_list)
    symbols_and_functions_list = findall('\W|[a-z]+\w{2}|[a-z]+\d{1}', string)
    result = string
    return symbols_and_functions_list


def merging_pluses_and_minuses(input_string: str) -> str:
    """It merges '+-' and '-+' in '-' and '--' in '+' """
    flag = True
    while flag:
        flag = False
        if '+-' in input_string:
            input_string = input_string.replace('+-', '-')
            flag = True
        if '-+' in input_string:
            input_string = input_string.replace('-+', '-')
            flag = True
        if '--' in input_string:
            input_string = input_string.replace('--', '+')
            flag = True
        if '++' in input_string:
            input_string = input_string.replace('++', '+')
            flag = True
    return input_string


s = 'log10(100)+---+log2(4)'
print(pycalc(s))
