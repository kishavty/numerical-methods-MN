znak = '0'
wykladnik = '01111111'
czesc_ulamk = '10110011001100110011001'

wykladnik_1 = 0
czesc_ulamk_1 = 0

for bit in range(len(wykladnik)):
    wykladnik_1 += int(wykladnik[len(wykladnik) -1 -bit]) *2**bit

for bit in range(len(czesc_ulamk)):
    czesc_ulamk_1 += int(czesc_ulamk[bit]) * (2**(-bit-1))


approx = (-1)**int(znak) * 2**(wykladnik_1-127) * (czesc_ulamk_1 + 1)

actual_value = 1.7
absolute_error = abs(approx - actual_value)
relative_error = absolute_error / abs(actual_value)

print(f"Wartość liczby: {actual_value}")
print(f"Błąd bezwzględny: {absolute_error}")
print(f"Błąd względny: {relative_error}")