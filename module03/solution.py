import math


def sum_of_digits(n):
    num_str = str(abs(n))
    sumar = 0
    for i in range(len(num_str)):
        sumar += int(num_str[i])
    return sumar


def to_digits(n):
    fill = [int(i) for i in str(n)]
    return fill


def to_number(digits):
    num_str = [str(i) for i in digits]
    num_int = int("".join(num_str))
    return num_int


def count_vowels(str):
    sumar = 0
    fill = ("a", "e", "i", "o", "u", "y")
    for i in str:
        if i.lower() in fill:
            sumar += 1
    return sumar


def count_consonants(str):
    sumar = 0
    cons = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
    for i in str:
        if i.lower() in cons:
            sumar += 1
    return sumar


def prime_number(number):

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def fact_digits(n):
    sumar = 0
    mul = 1
    num = str(n)
    for k in range( len(num) ):
        mul = 1
        for i in range(1, ( int(num[k]) + 1) ):
            mul = i*mul
        sumar += mul
    return sumar



def fibonacci(n):

    if n == 1:
        return [1]
    lst = [1, 1]

    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2])
    return lst

def fib_number(n):
    num_str = [str(i) for i in fibonacci(n)]
    result = int("".join(num_str))
    return result


def palindrome(obj):
    pali = str(obj) == str(obj)[::-1]
    return pali



def char_histogram(string):
    list_fill = []
    for i in string:
        list_fill.append( string.count(i) )
        res = {k:v for k, v in zip( string, list_fill )}
    return res
