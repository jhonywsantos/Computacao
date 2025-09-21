'''Uma mochila nova com capacidade para transportar até 18 kg, ele deseja descobrir quantos podem ser levados na mochila sem exceder
esse limite. Escreva um programa que receba como entrada o peso de vários livros e exiba a quantidade de livros que podem ser carregados.
Dica: A entrada deve parar quando um novo livro exceder a capacidade da mochila.'''

capacidade_mochila = 18
total_peso = 0
quantidade_livros = 0
excesso_peso = 0
encerrar_entrada = False

while not encerrar_entrada and total_peso <= capacidade_mochila:
    peso_livro = int(input("Digite o peso do livro (ou -1 para encerrar): "))

    if peso_livro == -1:
        encerrar_entrada = True
    elif total_peso + peso_livro <= capacidade_mochila:
        total_peso += peso_livro
        quantidade_livros += 1
    else:
        excesso_peso = total_peso + peso_livro - capacidade_mochila
        encerrar_entrada = True

print(f"Luigi pode levar {quantidade_livros} livro(s) na mochila.")
if excesso_peso > 0:
    print(f"Excedeu {excesso_peso} kg da capacidade da mochila.")

