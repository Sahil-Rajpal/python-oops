# problem -1 : timing function decorators

import time
def timer(func):
    def wrapper(*args,**kwargs): # * args - unlimited arguments(tuple) ,, **kwargs --> unlimited keyword arguments(dictionary)
        start=time.time()
        result = func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer  # jiske upar decorator lagana  hai usko upar @ lagao
def example_function(n):
    time.sleep(n)


example_function(2)


# example - 2 :-> Debugging function calls
import functools
def debug(func):

    def wrapper(*args,**kwargs):
        args_value= ', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper # returning definition of wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name} ")


hello()
greet("chai",greeting="hanji")



# example -3 :-> cache return value

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_runing_function(a,b):
    time.sleep(4)
    return a+b

print(long_runing_function(2,3))
print(long_runing_function(2,3))
print(long_runing_function(4,3))

