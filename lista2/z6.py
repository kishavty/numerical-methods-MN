import numpy as np
#from z4 import gauss_elim, back_substitution

A = np.array([[3.50, 2.77, -0.76, 1.80],
              [-1.80, 2.68, 3.44, -0.09],
              [0.27, 5.07, 6.90, 1.61],
              [1.71, 5.45, 2.68, 1.71]])

b = np.array([[7.31],
             [4.23],
             [13.85],
             [11.55]])

n = len(A)

def gauss_elim(A, b):
    A_b = np.append(A, b, axis=1)

    for k in range(0, n-1):
        max_w = np.argmax(np.abs(A_b[k:,k])) + k #szuka abs(max) wiersz w kolumnie
        A_b[[k, max_w]] = A_b[[max_w, k]]

        for w in range(k+1, n):
            if A_b[k,k] != 0.0:
                ratio = A_b[w,k] / A_b[k,k]
                A_b[w] = A_b[w] - A_b[k]*ratio
            else:
                raise Exception("Dividing by zero")
    return A_b

def back_substitution(A_b):
    results = np.zeros(n)
    for i in range(n-1,-1,-1):
        if A_b[i,i] != 0.0:
            results[i] = (A_b[i, -1] - np.dot(A_b[i, i + 1:n], results[i + 1:])) / A_b[i, i]
        else:
            raise Exception("Dividing by zero")            
    return results


#gauss elimination
matrix = gauss_elim(A,b)
solved_matrix = back_substitution(matrix)
print(f"Gauss elimination result: {solved_matrix}")

#built in solve
print(f"Built in solver: {np.linalg.solve(A,b).T}")


det_gauss = 1.0
for i in range(n):
    det_gauss = det_gauss * matrix[i,i]
print(det_gauss)


print(np.linalg.det(A))
