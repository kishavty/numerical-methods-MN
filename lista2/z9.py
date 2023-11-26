import numpy as np 

A = np.array([[1.0, 3.0, -9.0, 6.0, 4.0],
               [2.0, -1.0, 6.0, 7.0, 1.0],
               [3.0, 2.0, -3.0, 15.0, 5.0],
               [8.0, -1.0, 1.0, 4.0, 2.0],
               [11.0, 1.0, -2.0, 18.0, 7.0]])

n = len(A)

I = np.identity(n) #macierz jednostkowa

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


#liczenie wyznacznika
matrix = gauss_elim(A, I)

det_gauss = 1.0
for i in range(n):
    det_gauss = det_gauss * matrix[i,i]


### wyniki

print(f"Wyznacznik wyliczony za pomocą eliminacji gaussa: {det_gauss}, Zaokrąglony do 10 liczb po przecinku: {round(det_gauss, 10)}")

det_builtin = np.linalg.det(A)
print(f"Wyznacznik wbudowana metoda: {det_builtin}, Zaokrąglony do 10 liczb po przecinku: {round(det_builtin, 10)}")

inverse_gauss = substitution(matrix)
print("Macierz odwrotna eliminacja Gaussa")
print(inverse_gauss)

print("Macierz odwrotna wbudowana metoda")
A_inv = np.linalg.inv(A)
print(A_inv)
