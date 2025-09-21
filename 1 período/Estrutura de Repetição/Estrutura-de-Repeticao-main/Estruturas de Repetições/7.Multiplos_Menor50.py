'''Escreva um programa que receba como entrada dois números e retorne a quantidade de números positivos menores que 50 que são múltiplos de ambos.'''

def contar_multiplos_positivos(numero1, numero2):
    contador = 0
    
    for i in range(1, 50):
        if i % numero1 == 0 and i % numero2 == 0 and i < 50:
            contador += 1
    return contador

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = contar_multiplos_positivos(numero1, numero2)

print(f"A quantidade de números positivos menores que 50, que são múltiplos de ambos é equivalente à: {resultado}")
