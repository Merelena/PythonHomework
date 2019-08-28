"""This is a main module with general functions

:author: Fyodorova Elena
"""
from re import findall
import pycalc.Data as Data
import argparse


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
            '[a-zA-Z]+|[a-zA-Z]+\\d+|\\d+[a-zA-Z]+',
            string):
        if function not in Data.FUNCTION_DICT:
            return "ERROR: '{0}' is unknown function or constant".format(function)
    # Searching for unknown number and letter combinations
    string = positive_and_negative(searching_for_constants(findall(
        '[0-9.]+|//|==|<=|=>|!=|[<>*/^%)(+-]|\\w+\\d+|\\w+|[^ ,\\[\\]\']', merging_pluses_and_minuses(string)
    )))
    # Merging pluses and minuses and searching for negative and positive numbers
    try:
        if len(string) <= 1:
            float(string[0])
    except ValueError:
        return 'ERROR: no expression'
    while len(string) != 1 or (string.count(float) - 1 == string.count(',')):
        if 'ERROR' in string:
            return string
        string = calculating_expression_in_brackets(string)
    # Calculating simple expressions in brackets and out of them or returns error message
    if string[0] != 'True' and string[0] != 'False':
        return float(string[0])
    elif string[0] == 'True':
        return True
    else:
        return False


def searching_for_constants(string: list) -> list:
    """Changes constants to relevant numbers"""
    for index, symbol in enumerate(string):
        if symbol in Data.CONSTANTS.keys():
            string[index] = str(Data.CONSTANTS[symbol])
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
    for index, symbol in enumerate(string[::]):
        if (symbol == '+' or symbol == '-') \
                and (string[index-1] in Data.OPERATION_SET or index == 0) \
                and (string[index+1].replace('.', '', 1).lstrip('-').isdigit()):
            if symbol == '-':
                string[index+1] = str(0 - float(string[index+1]))
            del string[index]
    return string


def raising_a_power(expression: list) -> list:
    """Returns result of raising a power"""
    while '^' in expression:
        index = len(expression) - expression[::-1].index('^') - 1
        expression[index-1] = str(Data.FIRST_STEP_PRIORITY['^'](
            float(expression[index-1]),
            float(expression.pop(index+1))))
        del expression[index]
    return expression


def inclusion_in_general_expression(string, expression: list, start, finish):
    """Embeds result of calculating expressions in general expression"""
    for index, number in enumerate(expression):
        if type(expression[index]) != bool:
            expression[index] = float(number)
    if string[start - 1] in Data.FUNCTION_DICT.keys():
        if string[start - 1] == 'fsum':
            expression = Data.FUNCTION_DICT[string[start - 1]](expression)
        else:
            expression = Data.FUNCTION_DICT[string[start - 1]](*expression)
        # For correct work of function 'fsum'
        string = string[:start - 1] + [str(expression)] + string[finish + 1:]
    elif len(expression) == 1:
        string = string[:start] + [str(expression[0])] + string[finish + 1:]
    else:
        return 'ERROR: something is lost'
    return string


def calculating_expression_in_brackets(string: list):
    """Calculates all expressions in brackets

    :param string: list type
    :return: gradual result of calculation expressions or error messages
    """
    simple_expression = []
    if '(' in string:
        start = len(string) - string[::-1].index('(') - 1   # Last entry of opening bracket
        finish = start
        for symbol in string[start:]:
            if symbol == ')':
                break
            simple_expression.append(symbol)   # Updating of simple expression in brackets
            finish += 1
            if simple_expression[0] == '(':
                del simple_expression[0]
    else:
        start = 0
        finish = len(string) - 1
        simple_expression = string
    # Calculates start of simple expression without opening bracket
    temp = positive_and_negative(simple_expression)   # Retests to negative and positive numbers
    finish -= len(simple_expression) - len(temp)   # Calculates finish of simple expression without closing bracket
    simple_expression = temp   # Updating of simple expression
    if '^' in simple_expression:
        simple_expression = raising_a_power(simple_expression)
    temp = 0   # For correct calculating of indexes in following cycle
    try:
        for action in Data.SIMPLE_ACTIONS:
            for index, symbol in enumerate(simple_expression[::]):
                if symbol in action.keys():
                    simple_expression[index-1-temp] = action[symbol](
                        float(simple_expression[index-1-temp]),
                        float(simple_expression[index+1-temp])
                    )
                    del simple_expression[index-temp]
                    del simple_expression[index-temp]
                    temp += 2
        # Calculates expressions from start to finish
            temp = 0
        string = inclusion_in_general_expression(string, simple_expression, start, finish)
    except IndexError:
        return 'ERROR: number is lost'
    except TypeError:
        return 'ERROR: wrong number of arguments'
    except ValueError:
        return 'ERROR: wrong syntax'
    return string


def main():
    parser = argparse.ArgumentParser(description='Pure-python command-line calculator.')
    parser.add_argument('EXPRESSION', help='expression to evaluate')
    print(pycalc(parser.parse_args().EXPRESSION))
