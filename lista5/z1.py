import matplotlib.pyplot as plt 
import numpy as np 

h = np.array([0, 3, 6]) #x
p = np.array([1.225, 0.905, 0.652]) #y

##################

#lagrange

def lagrange(x, xData, yData):
    n = len(xData)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x-xData[j]) / (xData[i] - xData[j])
        y = y + w*yData[i]
    return y

#neville

def neville(x_eval, x, y):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y

    for i in range(1, n):
        for j in range(1, i+1):
            Q[i,j] = ((x_eval - x[i-j]) * Q[i, j-1] - (x_eval - x[i]) * Q[i-1, j-1]) / (x[i] - x[i-j])
    return Q[-1, -1]


#newton

def divided_diff(x, y):
    n = len(x)
    coefficients = np.zeros(n)

    for i in range(n):
        coefficients[i] = y[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x[i] - x[i - j])

    return coefficients


def newton(x_eval, x, y):
    coefficients = divided_diff(x, y)
    n = len(x)
    result = coefficients[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (x_eval - x[i]) + coefficients[i]

    return result




heights_to_interpolate = np.linspace(0, 6, 100)

densities_interpolated_lagrange = [lagrange(height, h, p) for height in heights_to_interpolate]

densities_interpolated_neville = [neville(height, h, p) for height in heights_to_interpolate]

densities_interpolated_newton = [newton(height, h, p) for height in heights_to_interpolate]


#wbudowane

coefficients = np.polyfit(h, p, 2)

poly_function = np.poly1d(coefficients)

func_builtin = poly_function(heights_to_interpolate)


#####################

plt.figure(figsize=(8, 6))
plt.scatter(h, p, color='red', label='Dane')
plt.plot(heights_to_interpolate, densities_interpolated_lagrange, alpha = 0.6, label='Interpolacja Lagrange\'a')
plt.plot(heights_to_interpolate, densities_interpolated_neville, alpha = 0.6, label='Interpolacja Neville\'a', linestyle='--')
plt.plot(heights_to_interpolate, densities_interpolated_newton, alpha = 0.6, label='Interpolacja Newtona', linestyle=':')
plt.plot(heights_to_interpolate, func_builtin, alpha = 0.3, label='Met. wbudowana')
plt.xlabel('h (km)')
plt.ylabel('rho (kg/m^3)')
plt.title('Interpolacja gęstości powietrza')
plt.legend()
plt.grid(True)
plt.show()