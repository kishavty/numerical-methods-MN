import numpy as np

def oblicz(x):
    wynik = x/100 * 100 - x
    return wynik
    
t = np.arange(1,51,1)
res = []
for i in t:
    print(i, oblicz(i))
    if oblicz(i) != 0:
        res.append(i)
print("liczby podatne na błąd:,", res)