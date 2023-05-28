#the decorator which counts the time of function have worked

from time import sleep, time


def running_time(func):
    def inner():
        start = time()
        func()
        end = time()
        print(end - start)

    return inner



@running_time
def some_delay():
    #start = time()
    sleep(3)
    print("hello")
    #end = time()
    #print(end - start)

some_delay()


