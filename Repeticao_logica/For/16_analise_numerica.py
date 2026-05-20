lista = [24, 78, 12, 45, 99, 33, 56, 4, 87, 61]
for numero in lista:
 print(numero, end=" ")
print()
soma = 0

for num in lista:
    soma += num
print(f"Soma total dos valores da lista {soma}")
print()

media = soma/len(lista)
print(f"A média das lista é: {media}")
print()

maior_num= lista[0]
for i in lista:
 if i > maior_num :
  maior_num = i
print(f"O maior número dessa lista é {maior_num}")
print()

menor_num = lista[0]
for i in lista:
 if i < menor_num:
     menor_num = i
print(f"O menor número dessa lista é {menor_num}")
print()

qntd_pares = 0
for i in lista:
    if i % 2 == 0:
        qntd_pares+=1
print(f"Essa lista  tem  {qntd_pares} números PARES")
print()

qntd_impares = 0
for i in lista:
    if i % 2 == 1:
     qntd_impares+=1
print(f"Essa lista  tem  {qntd_impares} números ÍMPARES")




