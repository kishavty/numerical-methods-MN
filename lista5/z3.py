import matplotlib.pyplot as plt
import numpy as np
from z1 import lagrange, neville, newton

re = np.array([0.2, 2, 20, 200, 2000, 20000])
cd = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])


####### własna implementacja
re_to_interpolate = np.linspace(0, 20000, 100) 

re_interpolated_lagrange = [lagrange(r, re, cd) for r in re_to_interpolate]
re_interpolated_neville = [neville(r, re, cd) for r in re_to_interpolate]
re_interpolated_newton = [newton(r, re, cd) for r in re_to_interpolate]

coefficients = np.polyfit(re, cd, 2)
poly_function = np.poly1d(coefficients)
func_builtin = poly_function(re_to_interpolate)


#print("Współczynniki wielomianu:", coefficients)

def calculate_CD(reynolds, coeffs):
    return np.polyval(coeffs, np.log(reynolds))

re_to_find = [5, 50, 5000]

for reynolds in re_to_find:
    cd_value = calculate_CD(reynolds, coefficients)
    print(f"cD dla Re = {reynolds}: {cd_value}")


re_lagrange = [lagrange(r, re, cd) for r in re_to_find]
re_neville = [neville(r, re, cd) for r in re_to_find]
re_newton = [newton(r, re, cd) for r in re_to_find]
re_built = [poly_function(re_to_find)]


print(f'Re  =   {re_to_find}')
print(f'lagrange{re_lagrange}')
print(f'neville {re_neville}')
print(f'newton  {re_newton}')
print(f'builtin  {re_built}')

### wykres

plt.figure(figsize=(8, 6))
plt.scatter(re, cd, color='red', label='Dane')
plt.plot(re_to_interpolate, re_interpolated_lagrange, label='Interpolacja Lagrange\'a')
plt.plot(re_to_interpolate, re_interpolated_neville, label='Interpolacja Neville\'a', linestyle='--')
plt.plot(re_to_interpolate, re_interpolated_newton, label='Interpolacja Newtona', linestyle=':')
plt.plot(re_to_interpolate, func_builtin, alpha = 0.3, label='Met. wbudowana')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolacja')
plt.legend()
plt.grid(True)
plt.show()