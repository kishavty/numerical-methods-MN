import numpy as np
from z4 import gauss_elim, back_substitution

A = np.array([[0.0 , 0.0 , 0.0 , 0.0 , 1.0], #niewiadomymi są a_i, liczymy je jak 'x' w normalnych
     [1.0 , 1.0 , 1.0 , 1.0 , 1.0],
     [81.0 , 27.0 , 9.0 , 3.0 , 1.0],
     [625.0 , 125.0 , 25.0 , 5.0 , 1.0],
     [1296.0 , 216.0 , 36.0 , 6.0 , 1.0]])

b = np.array([[-1.0 , 1.0 , 3.0 , 2.0 , -2.0]]).T

n = len(A)

#gauss elimination
matrix = gauss_elim(A,b)

#back substitiution
solved_matrix = back_substitution(matrix)
print(f"Gauss elimination result: {solved_matrix}")

#wbudowany solve
print(f"Built in solver: {np.linalg.solve(A,b).T}")