'''Esse ano Robson pretende montar uma bela árvore de Natal na empresa. Ele combinou com os outros 20 funcionários de comprar tudo e
depois ratear o valor. Ele encontrou a árvore perfeita e três tipos. Escreva um programa que receba como entrada o valor da
árvore, a quantidade e o preço unitário de cada tipo de enfeite (observe o formato de
entrada), calcule e exiba o total gasto e o valor a ser pago por cada funcionário do setor.'''

valor_arvore = float(input("Digite qual o valor da árvore perfeita: "))
total_gasto = valor_arvore
quantidade_funcionarios = 20

for _ in range(quantidade_funcionarios):
    quantidade_enfeites = int(input(f"Digite a quantidade total de enfeites para o funcionário {_ + 1}: "))
    preco_enfeite = float(input("Digite o preço unitário dos enfeites: "))
    total_gasto += quantidade_enfeites * preco_enfeite

valor_por_funcionario = total_gasto / quantidade_funcionarios

# Exibe o resultado
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Valor a ser pago por cada funcionário: R${valor_por_funcionario:.2f}")

