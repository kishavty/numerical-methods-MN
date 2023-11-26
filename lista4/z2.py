import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.cosh(x) * np.cos(x) - 1

x_values = np.linspace(4, 8, 100)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = cosh(x) * cos(x) - 1')
plt.axhline(y=0, color='r', alpha=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x)')
plt.legend()
plt.grid(True)
plt.show()



def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def newton(f, a, b, tol=1.0e-9):
    n = int(math.ceil(math.log(abs(b - a)/tol)/math.log(2.0)))
    x = 4
    for i in range(n):
        if abs(f(x)) < tol:
            return x
        x = x - (f(x) / derivative(f, x))
    return x


print(newton(f, 4.0, 8.0))