import numpy as np

A = np.array([[0 , 0 , 2 , 1 , 2] ,
              [0 , 1 , 0 , 2 , -1] ,
              [1 , 2 , 0 ,-2 , 0 ] ,
              [0 , 0 , 0 , -1 , 1 ] ,
              [0 , 1 , -1 , 1 , -1]])

b = np.array([[1] ,
             [1] ,
             [-4] ,
             [-2] ,
             [-1]])

n = len(A)

### wlasna implementacja algorytmu eliminacji gaussa

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

#back substitiution
solved_matrix = back_substitution(matrix)
print(f"Gauss elimination result: {solved_matrix}")


#wbudowany solve
print(f"Built in solver: {np.linalg.solve(A,b).T}")
