'''Dado um número Y, imprima quantas vezes Y aparece em uma sequência. Sabendo que
as duas primeiras linhas correspondem a X (quantidade de números da sequência) e Y
(o número procurado).'''

def contar_aparições(y, sequencia):
    contador = 0
    for numero in sequencia:
        if numero == y:
            contador += 1
    return contador

quantidade_numeros = int(input("Digite a quantidade de números na sequência: "))
y = int(input("Digite o número procurado: "))

sequencia = []
for _ in range(quantidade_numeros):
    numero = int(input("Digite um número da sequência: "))
    sequencia.append(numero)

resultado = contar_aparições(y, sequencia)
print(f"O número {y} aparece na sequência {resultado} vezes.")
