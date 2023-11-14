import numpy as np
import matplotlib.pyplot as plt
import cProfile

def polynomial(x):
    return 6*x**4 + 5*x**3 - 13*x**2 + x + 1

coefficients = [6, 5, 13, 1, 0]

def horner_recursion(coefficients, degree, x):
    if degree == 0:
        return coefficients[0]
    else:
        return x * horner_recursion(coefficients, degree-1, x)
    
cProfile.run("horner_recursion")

plt.plot(np.arange(-10, 10.0001, 0.0001), horner_recursion(coefficients, 4, np.arange(-10, 10.0001, 0.0001)))
plt.title("Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.show()