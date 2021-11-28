from functools import wraps


def val_checker(f_lambda):
    def wrap_func(func):
        @wraps(func)
        def wrapper(num):
            if not f_lambda(num):
                msg = f'wrong val {num}'
                raise ValueError(msg)
            return num, func(num)

        return wrapper

    return wrap_func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


result = calc_cube(5)
print(f'{calc_cube.__name__}({result[0]}) = {result[1]}')
result = calc_cube(-5)
print(f'{calc_cube.__name__}({result[0]}) = {result[1]}')
