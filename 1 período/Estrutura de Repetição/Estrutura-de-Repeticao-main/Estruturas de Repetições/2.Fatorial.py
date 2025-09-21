'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=120'''

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

while True:
    print('OBS: DIGITE APENAS VALORES INTEIROS E POSITIVOS!!')
    numero = int(input("Digite o valor de um número que você deseja fatorar: "))
    if numero >= 0:
        print(f"O fatorial de {numero} é equivalente a: {fatorial(numero)}")
    else:
        print(f"O valor sugerido {numero}, não está definido para fatorar números negativos.")