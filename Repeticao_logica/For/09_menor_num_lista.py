numeros = [2, 5, 8, 11, 14, 17, 20, 1,  23, 26, 29]

Menor_numero = numeros[0]

for numero in numeros:
    if numero < Menor_numero:
        Menor_numero = numero


print(Menor_numero)
