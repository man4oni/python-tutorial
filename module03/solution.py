import math


def sum_of_digits(n):
    num_str = str(abs(n))
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])
    return sum


def to_digits(n):
    list = [int(i) for i in str(n)]
    return list


def to_number(digits):
    num_str = [str(i) for i in digits]
    num_int = int("".join(num_str))
    return num_int


def count_vowels(str):
    sum = 0
    list = ("a", "e", "i", "o", "u", "y")
    for i in str:
        if i.lower() in list:
            sum += 1
    return sum


def count_consonants(str):
    sum = 0
    cons = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z")
    for i in (str):
        if i.lower() in cons:
            sum += 1
    return sum


def prime_number(number):
    if number == 1:
        return True
    if number > 1:
        for i in range(2, number // 2):
            if number % i == 0:
                return False
        else:
            return True

def fact_digits(n):
    sum=0
    mul=1
    num = str(n)
    for k in range( len(num) ):
        mul=1
        for i in range(1,( int(num[k]) + 1) ):
            mul=i*mul
        sum+=mul
    return sum



def fibonacci(n):
        if n <= 0:
            return []
        if n == 1:
            return [1]
        lst = [1, 1]
        if n == 2:
            return lst
        for i in range(2, n):
            lst.append(lst[i-1] + lst[i-2])
        return lst

def fib_number(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    lst = [1,1]
    if n == 2:
        return lst
    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2])
        list = [str(i) for i in lst]
        list1 = int( "".join(list) )
    return list1


def palindrome(obj):
    pali = str(obj) == str(obj)[::-1]
    return pali


###########################
def char_histogram(string):
    list_fill = []
    for i in (string):
        list_fill.append( string.count(i) )
        dict = {k:v for k, v in zip( string, list_fill )}
    return dict
