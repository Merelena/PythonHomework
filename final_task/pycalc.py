from re import split, findall, sub
import Data


def pycalc(string: str):
    """Main function of calculator"""
    brackets_list = findall('[(-)]', string)  # Searching for brackets to check a balance of them
    if brackets_list.count('(') != brackets_list.count(')'):
        raise Exception('ERROR: brackets are not balanced')
    string = positive_and_negative(findall('[0-9.]+|//|==|<=|=>|!=|\D|[^ ]', merging_pluses_and_minuses(string)))
    while len(string) != 1:
        string = brackets_expressions(string)
    return string


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


def positive_and_negative(string: list) -> list:
    for index, symbol in enumerate(string[:-1]):
        if symbol == '+' or symbol == '-':
            if string[index-1] in Data.operation_set or index == 0:
                string[index+1] = symbol + string[index+1]
                del string[index]
    return string


def brackets_expressions(string: list):
    simple_expression = []
    if '(' in string:
        start = len(string) - string[::-1].index('(') - 1
        finish = start
        for symbol in string[start:]:
            if symbol == ')':
                break
            simple_expression.append(symbol)
            finish += 1
            if simple_expression[0] == '(': del simple_expression[0]
    else:
        start = 0
        finish = len(string) - 1
        simple_expression = string
    flag = False
    for action in Data.simple_actions:
        temp = 0
        for index, symbol in enumerate(simple_expression[1::2]):
            if symbol in action.keys():
                simple_expression[index*2-temp] = action[symbol](
                    float(simple_expression[index * 2 - temp]),
                    float(simple_expression[index * 2 + 2 - temp])
                )
                del simple_expression[index*2-temp+1]
                del simple_expression[index*2-temp+1]
                temp += 2
    string = string[:start] + [str(simple_expression[0])] + string[finish+1:]
    return string


s = '8//(8+6^(3 - 1)+8 % 4)-(7+6^8*2)'
print(pycalc(s))


