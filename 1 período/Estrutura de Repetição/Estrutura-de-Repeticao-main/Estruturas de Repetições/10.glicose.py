'''Escreva um programa que receba vários valores da taxa de glicose de Genival, até que o valor informado seja 0, 
e calcule a glicose média observada naquele dia.Caso esse valor seja inferior a 110, o programa deve exibir a men-
sagem "Glicose Normal". Caso seja 200 ou mais, a mensagem exibida deve ser “Glicose Muito Alta". Nos demais casos, 
o programa deve exibir “Glicose Alterada”.'''

soma_glicose = 0
contador_valores = 0
encerrar_entrada = False

while not encerrar_entrada:
    valor_glicose = float(input("Digite o valor da taxa de glicose (ou 0 para encerrar): "))

    if valor_glicose == 0:
        encerrar_entrada = True
    else:
        soma_glicose += valor_glicose
        contador_valores += 1

if contador_valores > 0:
    glicose_media = soma_glicose / contador_valores
    print(f"Glicose média: {glicose_media:.2f}")

    if glicose_media < 110:
        print("Glicose Normal")
    elif glicose_media >= 200:
        print("Glicose Muito Alta")
    else:
        print("Glicose Alterada")
else:
    print("Nenhum valor de glicose foi informado.")
