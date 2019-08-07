def square(num: int) -> dict:
    """ Creating a dictionary with squares of keys"""
    return {square_dict: square_dict ** 2 for square_dict in range(1, num + 1)}


print(square(5))