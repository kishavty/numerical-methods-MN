import numpy as np
import matplotlib.pyplot as plt
import cProfile

def polynomial(x):
    return 6*x**4+5*x**3-13*x**2+x+1

def poly_res():
    results = []
    for x in np.arange(-10, 10.0001, 0.0001):
        results.append(polynomial(x))
    return results


cProfile.run("poly_res")

plt.plot(np.arange(-10, 10.0001, 0.0001), poly_res())
plt.title("Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.show()