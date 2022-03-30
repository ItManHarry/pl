def decorator(func):
    def wrapper(*args, **kwargs):
        print('-' * 8, 'begin', '-' * 8)
        f = func(*args, **kwargs)
        print(f)
        print('-' * 8, 'end', '-' * 8)
    return wrapper
'''
参数式装饰器，需要二次包装装饰器
'''
from functools import wraps
def decorator2(flag):
    def inner_decorator(function):
        @wraps(function)
        def real_decorator(*args, **kwargs):
            print('Flag is : ', flag)
            return function(*args, **kwargs)
        return real_decorator
    return inner_decorator
@decorator
def add_two(x, y):
    return x + y
@decorator2(2)
def add_three(x, y, z):
    return x + y + z
add_two(3, 5)
add_three(3, 5, 7)