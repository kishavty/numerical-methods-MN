import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,400)

z1 = (6 - 2 * x) / 6 + 4 * x + x**2
z2 = (6 - 4 * x + x**2) / 6 + 2 * x 


#Dwa przybliżenia Pade na jednym rysunku
plt.figure(figsize=(10, 5))
plt.plot(x, np.exp(-x), label='exp(-x)', linestyle='-', color='b', linewidth=2)
plt.plot(x, (6 - 2 * x) / (6 + 4 * x + x**2), label='z1', linestyle='--', color='r', linewidth=2)
plt.plot(x, (6 - 4 * x + x**2) / (6 + 2 * x ) , label='z2', linestyle='-.', color='g', linewidth=2)
plt.title('Przybliżenia Padé funkcji exp(-x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
#Zapisz wykres
#plt.savefig('dwaprzyblizenia.png')
#plt.savefig('dwaprzyblizenia.pdf')
#plt.close()


#Osobne przybliżeniami Pade
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(x, np.exp(-x), label='exp(-x)', linestyle='-', color='b', linewidth=2)
plt.plot(x, (6 - 2 * x) / (6 + 4 * x + x**2), label='z1', linestyle='--', color='r', linewidth=2)
plt.title('Przybliżenie Padé z1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x, np.exp(-x), label='exp(-x)', linestyle='-', color='b', linewidth=2)
plt.plot(x, (6 - 2 * x + x**2) / (6 + 2 * x ), label='z2', linestyle='-.', color='g', linewidth=2)
plt.title('Przybliżenie Padé z2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

#Zapisz wykres
#plt.savefig('dwaprzyblizeniaosobno.png')
#plt.savefig('dwaprzyblizeniaosobno.pdf')
#plt.close()

# Błąd przybliżenia
error1 = np.abs(np.exp(-x) - z1)
error2 = np.abs(np.exp(-x) - z2)

plt.figure(figsize=(10, 5))
plt.plot(x, error1, label='Błąd z1', linestyle='--', color='r', linewidth=2)
plt.plot(x, error2, label='Błąd z2', linestyle='-.', color='g', linewidth=2)
plt.title('Błąd przybliżeń')
plt.xlabel('x')
plt.ylabel('Błąd')
plt.legend()
plt.grid(True)
plt.show()

#Zapisz wykres
#plt.savefig('bladprzyblizenia.png')
#plt.savefig('bladprzyblizenia.pdf')
#plt.close()
