import numpy as np

def gauss_seidel(A, b, n, tol=1e-10, max_iter=1000):
    x = np.zeros(n)
    prev_x = np.zeros(n)
    iteration = 0
    
    while iteration < max_iter:
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], prev_x[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x - prev_x) < tol:
            return x, iteration + 1
        
        prev_x = np.copy(x)
        iteration += 1
    
    return x, iteration

############
#rownanie Ax = b
n = 10
A = np.zeros((n, n))
b = np.zeros(n)

for i in range(n):
    A[i, i] = 4
    if i > 0:
        A[i, i-1] = -1
    if i < n - 1:
        A[i, i+1] = -1
    if i == n - 1:
        b[i] = 100
A[0, n-1] = 1
A[n-1, 0] = 1

#print(A, b)
solution, iterations = gauss_seidel(A, b, n)

print(solution)
print("Liczba iteracji:", iterations)