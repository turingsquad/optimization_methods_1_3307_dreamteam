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

