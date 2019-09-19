def f_c(x):
    '''returns constant 4 '''
    return 4


def f_x(x, a, b):
    '''Write a function f_x(x, a, b) which implements the formula f(x) = a*x + b!'''
    return a * x + b


def sum(x):
    ''' Write a function sum(x) which returns the sum of f_x() called 3 times with parameters x, 1, 1, x, 2, 2, x, 3, 3!'''
    return f_x( x,1,1 )+f_x(x, 2,2 )+f_x(x, 3,3 )
