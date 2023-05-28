#the decorator which counts the time of function have worked

from time import sleep, time


def running_time(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result

    return inner




@running_time
def some_delay2(a, b):
    sleep(1)
    print("hello")
    return a + b

x = some_delay2(2, 3)
print("x = ", x)