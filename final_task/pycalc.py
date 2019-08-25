"""This is a main module with general functions

:author: Fyodorova Elena
"""
from re import split, findall, sub
import Data


def pycalc(string: str):
    """Main function

    :param string: input expression
    :type string: str
    :return: result of calculation or error message
    """
    brackets_list = findall('[(-)]', string)  # Searching for brackets to check a balance of them
    if brackets_list.count('(') != brackets_list.count(')'):
        return 'ERROR: brackets are not balanced'
    for function in findall(
            '[a-zA-Z]+|[a-zA-Z]+\d+|\d+[a-zA-Z]+',
            string):
        if function not in Data.function_dict:
            return "ERROR: '{0}' is unknown function or constant".format(function)
    # Searching for unknown number and letter combinations
    string = positive_and_negative(searching_for_constants(findall(
        '[0-9.]+|//|==|<=|=>|!=|[<>*/^%)(+-]|\w+\d+|\w+|[^ ,\[\]]', merging_pluses_and_minuses(string)
    )))
    # Merging pluses and minuses and searching for negative and positive numbers
    try:
        if len(string) <= 1:
            float(string[0])
    except ValueError:
        return 'ERROR: no expression'
    while len(string) != 1 or (string.count(float) - 1 == string.count(',')):
        if 'ERROR' in string: return string
        string = brackets_expressions(string)   # Calculation of simple expressions in brackets and out of them
    if string[0] != 'True' and string[0] != 'False':
        return float(string[0])
    elif string[0] == 'True': return True
    else: return False


def searching_for_constants(string: list) -> list:
    """Changes constants to relevant numbers"""
    for index, symbol in enumerate(string):
        if symbol in Data.constants.keys():
            string[index] = str(Data.constants[symbol])
    return string


def merging_pluses_and_minuses(input_string: str) -> str:
    """It merges '+-' and '-+' in '-' and '--' in '+' """
    flag = True   # Stops cycle of merging
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
    """Searches for positive and negative numbers"""
    for index, symbol in enumerate(string[:-1]):
        if (symbol == '+' or symbol == '-') \
                and (string[index-1] in Data.operation_set or index == 0) \
                and (string[index+1][0].isdigit() or string[index+1][1].isdigit()):
            if symbol == '-':
                string[index+1] = str(0 - float(string[index+1]))
            del string[index]
    return string


def brackets_expressions(string: list):
    """Calculates all expressions

    :param string: list type
    :return: gradual result of calculation expressions or error messages
    """
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
    # Calculates start of simple expression without opening bracket
    temp = positive_and_negative(simple_expression)   # Retests to negative and positive numbers
    finish -= len(simple_expression) - len(temp)   # Calculates finish of simple expression without closing bracket
    simple_expression = temp   # Updating of simple expression
    while '^' in simple_expression:
        index = len(simple_expression) - simple_expression[::-1].index('^') - 1
        simple_expression[index-1] = str(Data.first_step_priority['^'](
            float(simple_expression[index-1]),
            float(simple_expression.pop(index+1))))
        del simple_expression[index]
    # Calculates expressions with '^'
    temp = 0   # For correct calculating of indexes in following cycle
    try:
        for action in Data.simple_actions:
            for index, symbol in enumerate(simple_expression[::]):
                if symbol in action.keys():
                    simple_expression[index-1-temp] = action[symbol](
                        float(simple_expression[index-1-temp]),
                        float(simple_expression[index+1-temp])
                    )
                    del simple_expression[index-temp]
                    del simple_expression[index-temp]
                    temp += 2
        # Calculates all expressions from start to finish
            temp = 0
        for index, number in enumerate(simple_expression):
            if type(simple_expression[index]) != bool:
                simple_expression[index] = float(number)
        if string[start-1] in Data.function_dict.keys():
            if string[start-1] == 'fsum':
                simple_expression = Data.function_dict[string[start-1]](simple_expression)
            else:
                simple_expression = Data.function_dict[string[start - 1]](*simple_expression)
            string = string[:start-1] + [str(simple_expression)] + string[finish+1:]
        elif len(simple_expression) == 1:
            string = string[:start] + [str(simple_expression[0])] + string[finish+1:]
        else: return 'ERROR: something is lost'
        # For correct work of function 'fsum'
    except IndexError:
        return 'ERROR: number is lost'
    except TypeError:
        return 'ERROR: wrong number of arguments'
    except ValueError:
        return 'ERROR: wrong syntax'
    return string
