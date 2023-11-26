import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

##plot
plt.plot(np.linspace(1.6, 2.1, 100), [np.tan(np.pi - x) - x for x in np.linspace(1.6, 2.1, 100)], label = "np.tan(np.pi - x) - x")
plt.axhline(0, color = "r", label = "0")
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x)')
plt.legend()
plt.show()


def func(x):
    return np.tan(np.pi - x) - x


# metoda bisekcji

def bisection(f, x1, x2, switch=1, tol=1.0e-9):
    """
    Bisection method to find the root of a given function within an interval.

    Parameters:
    f (function): The function for which the root is to be found.
    x1 (float): Left endpoint of the interval.
    x2 (float): Right endpoint of the interval.
    switch (int, optional): Parameter for switch condition. Defaults to 1.
    tol (float, optional): Tolerance. Defaults to 1.0e-9.
    
    Raises:
    ValueError: If the signs of the function at both endpoints are the same.

    Returns:
    tuple or float: Root of the function (if found), function value at the root, and the number of iterations.
    """
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if np.sign(f1) == np.sign(f2):
        raise ValueError("Zły przedział x1-x2")
    
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))

    i = 0
    while True:
        x3 = 0.5*(x1 + x2)
        f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if np.sign(f2)!= np.sign(f3):
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3

        if  abs(f(x3)) < tol:
            break
        i += 1

    return x3, f(x3), i


# metoda brenta

def brent(f, x1, x2, tol=1.0e-9):
    """
    Brent's method to find the root of a given function within an interval.

    Parameters:
    f (function): The function for which the root is to be found.
    x1 (float): Left endpoint of the interval.
    x2 (float): Right endpoint of the interval.
    tol (float, optional): Tolerance. Defaults to 1.0e-9.
    
    Raises:
    ValueError: If the signs of the function at both endpoints are the same.

    Returns:
    tuple or float: Root of the function (if found), function value at the root, and the number of iterations.
    """
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if np.sign(f1) == np.sign(f2):
        raise ValueError("Zły przedział x1-x2")
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))

    for i in range(n):
        x3 = (x1 + x2) / 2.0
        f3 = f(x3)
        if f3 == 0.0:
            return x3
        if (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
            return None
        
        x = - (x1*f2*f3*(f2 - f3) + x2*f3*f1*(f3 - f1) + x3*f1*f2*(f1 - f2)) / ((f1 - f2)*(f2 - f3)*(f3 - f1))

        if  abs(f(x)) < tol:
            break

        if np.sign(f2)!= np.sign(f3):
            if x3 < x < x2:
                x1 = x3
                f1 = f3
            else:
                x2 = x3
                f2 = f3
    return x, f(x), i


### metoda siecznych

def chord(f, a, b): #cieciwa
    """
    Approximates the root by iteratively intersecting the x-axis with the line between the points (a, f(a)) and (b, f(b)).

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.

    Returns:
    float: Approximated root value.
    """
    return a - ( f(a)*(b-a) / (f(b) - f(a)) )

def falsi(f, a, b, tol=1.0e-9):
    """
    Falsi method to find the root of a given function within an interval.

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.
    tol (float, optional): Tolerance. Defaults to 1.0e-9.
    
    Raises:
    ValueError: If the signs of the function at both endpoints are the same.

    Returns:
    float: Root of the function (if found).
    """
    x = chord(f, a, b)
    n = int(math.ceil(math.log(abs(b - a)/tol)/math.log(2.0)))
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("Zły przedział a-b")

    for i in range(n):
        if f(x) == 0:
            return x
        if np.sign(f(x)) != np.sign(f(a)):
            x = chord(f, a, x)
            b = x
        else:
            x = chord(f, x, b)
            a = x
    return x


def secant(f, a, b, tol=1.0e-9): #sieczna
    """
    Secant method to find the root of a given function within an interval.

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.
    tol (float, optional): Tolerance. Defaults to 1.0e-9.
    
    Raises:
    ValueError: If the signs of the function at both endpoints are the same.

    Returns:
    tuple or float: Root of the function (if found), function value at the root, and the number of iterations.
    """
    x = chord(f, a, b)

    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("Zły przedział a-b")
    
    i = 0

    while True:
        if f(x) == 0:
            return x
        x = chord(f, a, x)
        if  abs(f(x)) < tol:
            break
        i += 1
    return x, f(x), i

### metoda newtona

def derivative(f, x, h=1e-5):
    """
    Approximates the derivative of a function at a given point using the finite difference method.

    Parameters:
    f (function): The function for which the derivative is to be approximated.
    x (float): The point at which the derivative is approximated.
    h (float, optional): The step size. Defaults to 1e-5.

    Returns:
    float: Approximated derivative value at the given point.
    """
    return (f(x + h) - f(x)) / h


def newton(f, a, b, tol=1.0e-9):
    """
    Newton's method to find the root of a given function within an interval.

    Parameters:
    f (function): The function for which the root is to be found.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.
    tol (float, optional): Tolerance. Defaults to 1.0e-9.

    Raises:
    ValueError: If the signs of the function at both endpoints are the same.

    Returns:
    tuple or float: Root of the function (if found), function value at the root, and the number of iterations.
    """
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("Zły przedział a-b")
    
    x = a #poczatkowe x
    i = 0

    while True:
        if abs(f(x)) < tol:
            return x
        
        x = x - (f(x) / derivative(f, x))

        if  abs(f(x)) < tol:
            break

        i += 1
    return x, f(x), i

# built in
y = lambda x: np.tan(np.pi - x) - x


result_builtin = fsolve(y, [2, 3])
result_bisection = bisection(func, 1.6, 2.1)
result_brent = brent(func, 1.6, 2.1)
result_secant = secant(func, 1.6, 2.1)
result_newton = newton(func, 1.6, 2.1)

print(f"Built-in: x = {result_builtin[0]},  f(x) = {func(result_builtin[0])}") #hybrd and hybrj algorithms
print(f"Bisekcja: x = {result_bisection[0]},  f(x) = {result_bisection[1]},  iteracje = {result_bisection[2]},  flops = 62") #iteracje * 2 (mnoz i dod) + 3*2 wywolania funkcji??
print(f"Brent:    x = {result_brent[0]}, f(x) = {result_brent[1]},  iteracje = {result_brent[2]},  flops = 650") # 23*iteracje + 3*2 wyw. funkcji
print(f"Sieczne:  x = {result_secant[0]}, f(x) = {result_secant[1]}, iteracje = {result_secant[2]}, flops = 1188") # 5*iteracje + 5 + 1*3 wyw funkcji?
print(f"Newton:   x = {result_newton[0]}, f(x) = {result_newton[1]}, iteracje = {result_newton[2]},   flops = 48") # 3*2*iteracje + 3*2 wyw funkcji
