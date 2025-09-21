'''Faça um programa que leia 20 valores e imprima a soma dos valores pares e dos valores ímpares.'''

soma_pares = 0
soma_impares = 0

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f"A soma dos números pares resulta em: {soma_pares} e a soma dos números ímpares resulta em: {soma_impares}")



