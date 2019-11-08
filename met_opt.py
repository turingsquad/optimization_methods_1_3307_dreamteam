import math

output_file = open("./output/met_opt.txt", "w")

def f(x):
    return math.cos(x)


def dichotomy_method(a, b, eps=1e-4):
    output_file.write("dichotomy_method\n")
    sigma = eps / 2.0
    x = (a + b) / 2.0
    i = 0
    while abs(b - a) > eps:
        i += 1
        x1 = x - sigma
        x2 = x + sigma
        output_file.write("i: " + str(i) + " a: " + str(a) + " b: " + str(b) + " x1: " + str(x1) + " f(x1): " 
                            + str(f(x1)) + " x2: " + str(x2) + " f(x2): " + str(f(x2)) + "\n")
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
    i = 0
    output_file.write("golden_section_method\n")
    while abs(b - a) > eps:
        i += 1
        x1 = a + 0.381966011 * (b - a)
        x2 = a + 0.618003399 * (b - a)
        output_file.write("i: " + str(i) + " a: " + str(a) + " b: " + str(b) + " x1: " + str(x1) + " f(x1): " 
                            + str(f(x1)) + " x2: " + str(x2) + " f(x2): " + str(f(x2)) + "\n")
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
    output_file.write("fibonacci_method\n")
    while (a+b) / e  >= fibonacci(i):
        i += 1
    i -= 1
    fib0 = fibonacci(i - 2)
    fib1 = fibonacci(i - 1)
    fib2 = fibonacci(i)
    iter = 1
    x1 = a + fib0 / fib2 * (b - a)
    x2  = a + fib1 / fib2 * (b - a)
    output_file.write("i: " + str(iter) + " a: " + str(a) + " b: " + str(b) + " x1: " + str(x1) + " f(x1): " 
                            + str(f(x1)) + " x2: " + str(x2) + " f(x2): " + str(f(x2)) + "\n")
    while b - a > e:
        iter += 1
        x1 = a + fib0 / fib2 * (b - a)
        x2  = a + fib1 / fib2 * (b - a)
        output_file.write("i: " + str(iter) + " a: " + str(a) + " b: " + str(b) + " x1: " + str(x1) + " f(x1): " 
                            + str(f(x1)) + " x2: " + str(x2) + " f(x2): " + str(f(x2)) + "\n")
        if f(x1) < f(x2):
            b = x2
        elif f(x1) > f(x2):
            a  = x1
        else:
            a = x1
            b = x2
    return (x1 + x2) / 2


def line_search(x0, sigma):
    output_file.write("line_search\n")
    x1 = 0
    h = 0
    if f(x0) > f(x0 + sigma):
        x1 = x0 + sigma
        h = sigma
    elif f(x0) > f(x0 - sigma):
        x1 = x0 - sigma
        h = -sigma
    h *= 2
    x = x1
    x_nxt = x + h
    x_prev = x0
    it = 1
    output_file.write("i: " + str(it) + " left_border: " + str(x_prev) + " right_border: " 
                        + str(x_nxt) + " f(x_nxt): " + str(f(x_nxt)) + " x: " + str(x) + " f(x): " + str(f(x)) + " h: " + str(h))
    while f(x) > f(x_nxt):
        it += 1
        h *= 2
        x_prev = x
        x = x_nxt
        x_nxt = x + h
        output_file.write("i: " + str(it) + " left_border: " + str(x_prev) + " right_border: " 
                        + str(x_nxt) + " x: " + str(x) + " h: " + str(h))
    return [x_prev, x_nxt]


dichotomy_method(0, math.pi)
golden_section_method(0, math.pi)
fibonacci_method(0, math.pi)
line_search(0, math.pi)