from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num = kwargs['x']
        res = (f'{num}: {type(num)}', func(num))
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


result = calc_cube(x=5)
print(f'{calc_cube.__name__}({result[0]}) = {result[1]}')
