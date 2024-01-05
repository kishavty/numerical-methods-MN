import numpy as np
import matplotlib.pyplot as plt

T = np.array([0, 21.1, 37.8, 54.4, 71.1, 87.8, 100])
mu_k = np.array([1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296])
temperatures_to_find = [10, 30, 60, 90]

coefficients = np.polyfit(T, mu_k, 3)

print("Współczynniki wielomianu:", coefficients)

def wbud_calculate_mu_k(temperature, coeffs):
    return np.polyval(coeffs, temperature)

for temp in temperatures_to_find:
    mu_k_value = wbud_calculate_mu_k(temp, coefficients)
    print(f"wbudowane mu_k dla T = {temp} C: {mu_k_value}")



############
    
#metoda najmniejszych kwadratów
    
n = 3  #stopien wielomianu
N = len(T)
X = np.zeros((n + 1, n + 1))
Y = np.zeros(n + 1)

for i in range(n + 1):
    for j in range(n + 1):
        X[i, j] = np.sum(T ** (i + j))
    Y[i] = np.sum(mu_k * (T ** i))

def calculate_mu_k(temperature, coeffs):
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * (temperature ** i)
    return result



coefficients_2 = np.linalg.solve(X, Y)

print("Współczynniki wielomianu:", coefficients_2)

for temp in temperatures_to_find:
    mu_k_value = calculate_mu_k(temp, coefficients_2)
    print(f"wlasne mu_k dla T = {temp} C: {mu_k_value}")



########
    
x = np.linspace(0, 100, 100)
plt.scatter(T, mu_k, color='red', label='Dane')
plt.plot(x, calculate_mu_k(x, coefficients_2), label = 'met. najmn. kwadratow')
plt.plot(x, wbud_calculate_mu_k(x, coefficients), linestyle = ':', label = 'met. wbudowana')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja')
plt.legend()
plt.grid(True)
plt.show()