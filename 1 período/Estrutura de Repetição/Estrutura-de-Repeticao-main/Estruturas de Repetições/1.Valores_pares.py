'''Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.'''

valores = []
pares = 0
impares = 0
for i in range(5):
    valor = int(input("Digite um número: "))
    valores.append(valor)
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

for valor in valores:
    if valor % 2 == 0:
        print(f"O valor {valor} faz parte dos números pares.")
    else:
        print(f"O número {valor} faz parte dos números ímpares.")

print(f"A quantidade de números pares se refere à: {pares}")
print(f"A quantidade de números ímpares se refere à: {impares}")
