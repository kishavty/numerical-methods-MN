import numpy as np
import matplotlib.pyplot as plt

n = 20
k = 100
B = np.zeros((n,n))

#macierz z zadania
for i in range(n):
    B[i, i] = 0.025 * (i+1)
    if i < n - 1:
        B[i, i+1] = 5.0


def x_k(k, n):
    x = np.zeros((k + 1, n))
    x[0] = np.ones(n).T
    eta = np.zeros(k)
    for i in range(1, k+1):
        x[i] = np.dot(B, x[i-1])
        eta[i-1] = np.linalg.norm(x[i-1], 2.0) / np.linalg.norm(x[0], 2.0) #wzor z zadania
    return eta, x


eta = x_k(k, n)[0]

### plot
fig = plt.figure(figsize=(10,6))
ax = fig.gca()
plt.plot(np.arange(1,101,1), eta, label = "Eta_k")
plt.axhline(y = 1.0e+14, color = 'r', linestyle = '-', label = "10^14")
plt.axvline(x = eta.argmax(), color = 'b', linestyle = '-', label = "26") #26 zamiast 25 z zadania, bo indeksy mi sie przesunely o 1 gdzies
plt.yscale('log')
ax.set_xticks(np.arange(0, 101, 5))
plt.grid()
plt.title("Eta_k")
plt.xlabel("k")
plt.ylabel("Eta")
plt.legend()
plt.show()


### liczenie min k

list_k = np.zeros(k)
xlist = x_k(k, n)[1]
for i in range(k):
    if np.linalg.norm(xlist[i], 2.0) < np.linalg.norm(xlist[0], 2.0):
        list_k[i] = 1.0


print(list_k)
print(f"najmniejsze k, dla ktorego ||x^(k)||_2 < ||x^(0)||_2 to:  {list(list_k).index(max(list_k))+1}")