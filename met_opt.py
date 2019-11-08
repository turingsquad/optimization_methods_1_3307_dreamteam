import math


def f(x):
    return math.cos(x)


def dichotomy_method(a, b, eps=1e-4):
    sigma = eps / 2.0
    x = (a + b) / 2.0
    while abs(b - a) > eps:
        x1 = x - sigma
        x2 = x + sigma
        if f(x1) < f(x2):
            b = x1
        elif f(x1) > f(x2):
            a = x2
        else:
            a = x1
            b = x2
        x = (a + b) / 2.0
    return x


def golden_section_method(a, b, eps=1e-4):
    while abs(b - a) > eps:
        x1 = a + 0.381966011 * (b - a)
        x2 = a + 0.618003399 * (b - a)
        if f(x1) < f(x2):
            b = x1
        elif f(x1) > f(x2):
            a = x2
        else:
            a = x1
            b = x2
    return (a + b) / 2.0

def fibonacci(n):
    return int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))

def fibonacci_method(a, b, e = 1e-4, i = 0):
    while (a+b) / e  >= fibonacci(i):
        i += 1
    i -= 1
    fib0 = fibonacci(i - 2)
    fib1 = fibonacci(i - 1)
    fib2 = fibonacci(i)
    x1 = a + fib0 / fib2 * (b - a)
    x2  = a + fib1 / fib2 * (b - a)
    while b - a > e:
        x1 = a + fib0 / fib2 * (b - a)
        x2  = a + fib1 / fib2 * (b - a)
        if f(x1) < f(x2):
            b = x2
        elif f(x1) > f(x2):
            a  = x1
        else:
            a = x1
            b = x2
    return (x1 + x2) / 2


def line_search(x0, sigma):
    x1 = 0
    h = 0
    if f(x0) > f(x0 + sigma):
        x1 = x0 + sigma
        h = sigma
    elif f(x0) > f(x0 - sigma):
        x1 = x0 - sigma
        h = -sigma
    h *= 2
    x_k = x1
    x_k1 = x_k + h  #xk+1
    xk1 = x0        #xk-1
    while f(x_k) > f(x_k1):
        h *= 2
        xk1 = x_k
        x_k = x_k1
        x_k1 = x_k + h
    return xk1, x_k1