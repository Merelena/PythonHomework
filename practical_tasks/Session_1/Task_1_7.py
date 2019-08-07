def foo(input_list: list) -> list:
    """ Creating result list """
    mult = 1
    result_list = []
    for item in input_list:
        mult *= item
    for item in input_list:
        result_list.append(mult // item)
    return result_list


print(foo([1, 2, 3, 4, 5]))