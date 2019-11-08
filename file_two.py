import math

def func(x):
    return (x[1] - x[0]**2)**2 + (1 - x[0])**2

def num_gradient(f, x1, x2, h=1e-6):
    der_1 = (f([x1 + h, x2]) - f([x1 - h, x2])) / (2 * h)
    der_2 = (f([x1, x2 + h]) - f([x1, x2 - h])) / (2 * h)
    return [der_1, der_2]

def an_gradient(f, x1, x2):
    der_1 = 2 * (2 * x1**3 - 2 * x1 * x2 + x1 - 1)
    der_2 = 2 * (x2 - x1**2)
    return [der_1, der_2]

def distance_between(x1, x2):
    dist = 0
    for i in range(len(x1)):
        dist += (x2[i] - x1[i])**2
    dist = math.sqrt(dist)
    return dist 

def calculate_len(vector):
    length = 0
    for i in vector:
        length += i ** 2
    length = math.sqrt(length)
    return length

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


def dichotomy_method(f, a, b, x, gradient, eps=1e-4):
    x1_temp = [0, 0]
    x2_temp = [0, 0]
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
        mid = (b + a) / 2.0
    return mid

def steepest_descent(f, x, gradient_func, eps=1e-2):
    x_prev = x.copy()
    x_new = [x_prev[0] + (eps * 2), x_prev[1] + (eps * 2)]
    i = 0
    while (abs(f(x_prev) - f(x_new)) > eps ) and (abs(distance_between(x_prev, x_new)) > eps):
        grad = gradient_func(f, x_prev[0], x_prev[1])
        grad_len = calculate_len(grad)
        grad = [grad[0]/grad_len, grad[1]/grad_len]
        h = golden_section_method(f, 0, 100000, x_prev, grad)
        x_temp = x_new.copy()
        x_new = [x_prev[0] - h * grad[0], x_prev[1] - h * grad[1]]
        x_prev = x_temp
        print("x_prev = " + str(x_prev) + " x_new = " + str(x_new) + " grad = " + str(grad))
        i += 1
    return x_new


print(str(steepest_descent(func, [20, 20], num_gradient)))