def combine_dicts(*args) -> dict:
    """ Combining dictionaries"""
    result_dict = args[0]
    for dictionary in args[1:]:
        for pair in dictionary.items():
            if pair[0] in result_dict.keys():
                result_dict[pair[0]] += pair[1]
            else:
                result_dict.update({pair[0]: pair[1]})
    return result_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2, dict_3))