cache = None


def cacher(func):
    visited = False
    def wrapper(*args, **kwargs):
        global cache
        nonlocal visited
        cache = func(*args, **kwargs)
        if not visited: return cache
        return cache
        visited = True
    return wrapper


@cacher
def foo(a):
    return a+2


print(foo(3), cache)