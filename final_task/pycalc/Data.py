"""This module exports arithmetic, COMPARISON and other auxiliary functions, dictionaries ans lists

:author: Fyodorova Elena
"""


import math


def addition(first_number: float, second_number: float) -> float:
    """Returns the sum of input numbers"""
    return first_number + second_number


def subtraction(first_number: float, second_number: float) -> float:
    """Returns the difference between input numbers"""
    return first_number - second_number


def multiplication(first_number: float, second_number: float) -> float:
    """Returns the multiplication of input numbers"""
    return first_number * second_number


def division(first_number: float, second_number: float) -> float:
    """Returns the quotient of input numbers"""
    return first_number / second_number if type(first_number) == float else 0 - second_number


def whole_division(first_number: float, second_number: float) -> float:
    """Returns the whole division of input numbers"""
    return first_number // second_number


def division_with_remainder(first_number: float, second_number: float) -> float:
    """Returns the division with remainder of input numbers"""
    return first_number % second_number


def less(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '<' of input numbers"""
    return first_number < second_number


def less_or_equal(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '<=' of input numbers"""
    return first_number <= second_number


def greater(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '>' of input numbers"""
    return first_number > second_number


def greater_or_equal(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '>=' of input numbers"""
    return first_number >= second_number


def unequal(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '!=' of input numbers"""
    return first_number != second_number


def equal(first_number: float, second_number: float) -> bool:
    """Returns the result of COMPARISON '==' of input numbers"""
    return first_number == second_number


FUNCTION_DICT = math.__dict__
FUNCTION_DICT.update({'round': round, 'abs': abs})
THIRD_STEP_PRIORITY = {'+': addition, '-': subtraction}
SECOND_STEP_PRIORITY = {
    '*': multiplication,
    '/': division,
    '//': whole_division,
    '%': division_with_remainder,
}
FIRST_STEP_PRIORITY = {'^': pow}
COMPARISON = {
    '<': less,
    '<=': less_or_equal,
    '>': greater,
    '>=': greater_or_equal,
    '!=': unequal,
    '==': equal
}
SIMPLE_ACTIONS = [SECOND_STEP_PRIORITY, THIRD_STEP_PRIORITY, COMPARISON]
CONSTANTS = {
    'e': math.e,
    'pi': math.pi,
    'tau': math.tau,
    'nan': math.nan,
    'inf': math.inf
}
OPERATION_SET = ('*', '/', '//', '%', '<', '>', '=', '(', '^')   # For searching for negative and positive numbers
