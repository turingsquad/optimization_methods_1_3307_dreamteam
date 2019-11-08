import math


def fibonacci(n):
    return int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))


def fibonacci_method(f, a, b, x, gradient, eps=1e-4, i = 0):
    x1_temp = [0, 0]
    x2_temp = [0, 0]

    while (a + b) / eps >= fibonacci(i):
        i += 1
    i -= 1
    fib0 = fibonacci(i - 2)
    fib1 = fibonacci(i - 1)
    fib2 = fibonacci(i - 3)
    x1 = 0
    x2 = 0
    while (b - a) > eps:
        x1 = a + fib0 / fib2 * (b - a)
        x2 = a + fib1 / fib2 * (b - a)
        for i in range(len(x)):
            x1_temp[i] = x[i] - x1*gradient[i]
            x2_temp[i] = x[i] - x2*gradient[i]
        if (f(x1_temp) < f(x2_temp)):
            b = x2
        elif f(x1) > f(x2):
            a = x1
        else:
            a = x1
            b = x2
    return (x1 + x2) / 2.0

def dichotomy_method(f, a, b, x, gradient, eps=1e-4):
    x1_temp = x2_temp = x
    sigma = eps / 2.0
    mid = (b + a) / 2.0
    while abs(b - a) > eps:
        x1 = mid - sigma
        x2 = mid + sigma
        for i in range(len(x)):
            x1_temp[i] = x[i] - x1 * gradient[i]
            x2_temp[i] = x[i] - x2 * gradient[i]
        if f(x1_temp) < f(x2_temp):
            b = x1
        elif f(x1_temp) > f(x2_temp):
            a = x2
        else:
            a = x1
            b = x2
        mid = abs(b - a) / 2.0
    return mid

def golden_section_method(f, a, b, x, gradient, eps=1e-4):
    x1_temp = [0, 0]
    x2_temp = [0, 0]
    while abs(b - a) > eps:
        x1 = a + 0.381966011 * (b - a)
        x2 = a + 0.618003399 * (b - a)
        for i in range(len(x)):
            x1_temp[i] = x[i] - x1 * gradient[i]
            x2_temp[i] = x[i] - x2 * gradient[i]
        if f(x1_temp) < f(x2_temp):
            b = x1
        elif f(x1_temp) > f(x2_temp):
            a = x2
        else:
            a = x1
            b = x2
    return (a + b) / 2.0


def line_search(f, x0, x, gradient, sigma):
    x1_temp = [0, 0]
    x2_temp = [0, 0]

    for i in range(len(x)):
        x1_temp[i] = x[i] - x0*gradient[i]
        x2_temp[i] = x[i] - (x0 + sigma)*gradient[i]

    if f(x1_temp) > f(x2_temp):
        x_temp = x0 + sigma
        h = sigma
    else:
        x_temp = x0 - sigma
        h = -sigma
    h *= 2
    x_nxt = x_temp + h
    x_prev = x0
    for i in range(len(x)):
        x1_temp[i] = x[i] - x_temp * gradient[i]
        x2_temp[i] = x[i] - x_nxt * gradient[i]
    while f(x1_temp) > f(x2_temp):
        h *= 2
        x_prev = x_temp
        x_temp = x_nxt
        x_nxt = x_temp + h
        for i in range(len(x)):
            x1_temp[i] = x[i] - x_temp * gradient[i]
            x2_temp[i] = x[i] - x_nxt * gradient[i]

    return [x_prev, x_nxt]