from typing import Dict, Union


def num_add(a, b):
    return a + b


def num_sub(a, b):
    return a - b


def num_mul(a, b):
    return a * b


def num_div(a, b):
    return a / b


def num_floor(a, b):
    return a // b


def num_rem(a, b):
    return a % b


IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {"flour": 2, "eggs": 4, "milk": 200, "butter": False, "salt": 0.001}


def ingredient_exists(ingr, dict):
    if ingr in dict:
        return IS_TRUE
    else:
        return IS_FALSE

def fatten_pancakes(dict):
    dict["eggs"]=6
    dict["butter"]=True
    return dict.copy()

def add_sugar(dict):
    dict["sugar"]=True
    return dict.copy()

def remove_salt(dict):
    dict.pop("salt")
    return dict.copy()

FIBONACCI_NUMBERS=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
    l=len(lst)
    lst.append(lst[l-1]+lst[l-2])
    return lst.copy()

def fib_exists(lst, n):
    if n in lst:
        return IS_TRUE
    else:
        return IS_FALSE

def which_fib(lst, n):
    if n<=1 & n in lst:
        return 1
    else:
        return lst.index(n)+1









