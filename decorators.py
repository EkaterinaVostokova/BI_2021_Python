#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
import random   
import requests

1. Напишите простой декоратор, подменивающий возвращаемое значение декорируемой функции на время её выполнения (Example_1). Для измерения времени воспользуйтесь модулем time. (3 балла)
# In[2]:


def measure_time(func):
    def f(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        return time.time() - start
    return f

@measure_time
def some_function(a, b, c, d, e=0, f=0, g="3"):
    time.sleep(a)
    time.sleep(b)
    time.sleep(c)
    time.sleep(d)
    time.sleep(e)
    time.sleep(f)
    return g

print(some_function(1, 2, 3, 4, e=5, f=6, g="99999"))

2. Напишите декоратор, позволяющий логировать запуски функций, распечатывая входные данные и тип возвращаемых значений (Example_2). Для получения имени класса в виде строки можно воспользоваться атрибутом __name__. (7 баллов)
# In[3]:


def function_logging(func):
    def func_log(*args, **kwargs):
        if args and kwargs:
            print(f"Function {func.__name__} is called with positional arguments: {args} and keyword arguments:",
                  ", ".join(f'{key}={value}' for key, value in kwargs.items()))
        elif args:
            print(f"Function {func.__name__} is called with positional arguments: {args}")
        elif kwargs:
            print(f"Function {func.__name__} is called with keyword arguments: ",
                  ", ".join(f'{key}={value}' for key, value in kwargs.items()))
        else:
            print(f"Function {func.__name__} is called with no arguments")
        print(f"Function {func.__name__} returns output of type {type(func(*args, **kwargs)).__name__}")
        return func(*args, **kwargs)
    return func_log

@function_logging
def func1():
    return set()

@function_logging
def func2(a, b, c):
    return (a + b) / c

@function_logging
def func3(a, b, c, d=4):
    return [a + b * c] * d

@function_logging
def func4(a=None, b=None):
    return {a: b}

print(func1(), end="\n\n")
print(func2(1, 2, 3), end="\n\n")
print(func3(1, 2, c=3, d=2), end="\n\n")
print(func4(a=None, b=float("-inf")), end="\n\n")

3. Сделайте декоратор - русскую рулетку, который сделает так, чтобы декорируемая функция с заданной вероятностью заменяла возвращаемое значение на переданное декоратору (Example_3). (7 баллов)
# In[5]:


def russian_roulette_decorator(probability, return_value="Ooops, your output has been stolen!"):
    def decorator(func):
        def f(*args, **kwargs):
            if random.random() < probability:
                return return_value
            else:
                return func(*args, **kwargs)
        return f
    return decorator

@russian_roulette_decorator(probability=0.2, return_value="Ooops, your output has been stolen!")
def make_request(url):
    return requests.get(url)
for _ in range(10):
    print(make_request("https://google.com"))   

