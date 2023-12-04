import numpy as np
import scipy.linalg as sl

n = 5
A = np.array(sl.hilbert(n))
b = np.array([5, 4, 3, 2, 1], dtype=np.float32).T

def iter_solve(A, b, n):
    LU, piv = sl.lu_factor(A) #rozklad LU
    x = np.zeros(n, dtype=np.float32) #float32 dla pojedynczej precyzji
    u = np.finfo(float).eps #jednostka maszynowa, tolerancja dla warunku zakonczenia iteracji, smallest representable number such that 1.0 + eps != 1.0.
    iterations = 0 
    while True:
        r = b - np.dot(A, x)
        if np.linalg.norm(r, np.inf) <= u * np.linalg.norm(b, np.inf) or iterations == 1000:  #inf:   max(sum(abs(x), axis=1))
            break
        delta_x = sl.lu_solve((LU, piv), r) #obliczanie poprawki
        x = x + delta_x

        iterations += 1
    return x


print(iter_solve(A,b,n))
