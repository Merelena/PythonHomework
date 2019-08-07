def mod(text:str) -> str:
    """ Looking for ' and " and changing to vice versa """
    tmp = text.maketrans('\'\"', '\"\'')
    result = text.translate(tmp)
    return result

print(mod('\'sdf\"\'ll\''))