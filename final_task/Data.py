import math


def addition(first_number: float, second_number: float) -> float:
    return first_number + second_number


def subtraction(first_number: float, second_number: float) -> float:
    return first_number - second_number


def multiplication(first_number: float, second_number: float) -> float:
    return first_number * second_number


def division(first_number: float, second_number: float) -> float:
    return first_number / second_number if type(first_number) == float else 0 - second_number


def whole_division(first_number: float, second_number: float) -> float:
    return first_number // second_number


def division_with_remainder(first_number: float, second_number: float) -> float:
    return first_number % second_number


def less(first_number: float, second_number: float) -> bool:
    return first_number < second_number


def less_or_equel(first_number: float, second_number: float) -> bool:
    return first_number <= second_number


def greater(first_number: float, second_number: float) -> bool:
    return first_number > second_number


def greater_or_equel(first_number: float, second_number: float) -> bool:
    return first_number >= second_number


def unequel(first_number: float, second_number: float) -> bool:
    return first_number != second_number


def equel(first_number: float, second_number: float) -> bool:
    return first_number == second_number


function_dict = math.__dict__
function_dict.update({'round': round, 'abs': abs})
third_step_priority = {'+': addition, '-': subtraction}
second_step_priority = {
    '*': multiplication,
    '/': division,
    '//': whole_division,
    '%': division_with_remainder,
}
first_step_priority = {'^': pow}
comparison = {
    '<': less,
    '<=': less_or_equel,
    '>': greater,
    '>=': greater_or_equel,
    '!=': unequel,
    '==': equel
}
simple_actions = [first_step_priority, second_step_priority, third_step_priority, comparison]
constants = {
    'e': math.e,
    'pi': math.pi,
    'tau': math.tau,
    'nan': math.nan,
    'inf': math.inf
}
operation_set = ('*', '/', '//', '%', '<', '>', '=', '(', '^')   # For searching for negative and positive numbers
