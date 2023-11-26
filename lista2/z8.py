import numpy as np

A = np.array([[2,-1,0,0,0,0],
                [-1,2,-1,0,0,0],
                [0,-1,2,-1,0,0],
                [0,0,-1,2,-1,0],
                [0,0,0,-1,2,-1],
                [0,0,0,0,-1,5]])

n = len(A)
I = np.identity(n)


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

def substitution(A_b):
    for k in range(n-1,-1,-1):
        A_b[k] = A_b[k] / A_b[k, k]
        for w in range(k - 1, -1, -1):
            A_b[w] = A_b[w] - A_b[k] * A_b[w, k]
    inverse = A_b[:, n:]
    return inverse    



matrix = gauss_elim(A, I)
inverse = substitution(matrix)
print("Inverse Matrix:")
print(inverse)


A_inv = np.linalg.inv(A)


print(A_inv)
