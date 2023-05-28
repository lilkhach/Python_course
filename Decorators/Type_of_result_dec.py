#the decorator which counts the time of function have worked

from time import sleep, time
from functools import wraps


def running_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(type(result))
        return result

    return inner




@running_time
def some_delay2(a, b):
    sleep(1)
    print("hello")
    return a + b

x = some_delay2(2, 3)
print("x = ", x)