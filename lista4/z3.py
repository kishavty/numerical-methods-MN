import numpy as np
import matplotlib.pyplot as plt
import math

u = 2510.0
M0 = 2.8e6
mdot = 13.3e3
g = 9.81
v_sound = 335.0

def v(t):
    return u * np.log(M0 / (M0 - mdot * t)) - g*t - v_sound

t_values = np.linspace(0, 100, 100)
y_values = v(t_values)

plt.figure(figsize=(8, 6))
plt.plot(t_values, y_values, label='u * np.log(M0 / (M0 - mdot * t)) - g*t')
plt.axhline(y=0, color='r', alpha=0.7, label="predkosc dzwieku 335")
plt.xlabel('t')
plt.ylabel('v(t)')
plt.title('Wykres funkcji v(t)')
plt.legend()
plt.grid(True)
plt.show()


def derivative(f, x, h=1e-9):
    return (f(x + h) - f(x)) / h


def newton(f, a, b, tol=1.0e-9):
    n = int(math.ceil(math.log(abs(b - a)/tol)/math.log(2.0)))
    x = a
    for i in range(n):
        if abs(f(x)) < tol:
            return x
        x = x - (f(x) / derivative(f, x))
    return x

print(f"Rakieta osiągnie prędkość dźwięku (335 m/s) w czasie t = {newton(v, 60.0, 80.0)} s")