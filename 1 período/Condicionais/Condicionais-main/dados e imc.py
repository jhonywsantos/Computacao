nome = input('digite o seu nome:')
altura_str = float(input('Digite sua altura: '))
altura = float(altura_str)
peso_str = float(input('digite o seu peso:'))
peso = float(peso_str)

Indice_massa_corporal = peso / altura **2
if Indice_massa_corporal<18.49: 
    print(f'\nSeu resultado é {Indice_massa_corporal:.2f}, você está abaixo do peso, tem que se alimentar mais {nome}!' )
elif 18.49 <= Indice_massa_corporal < 24.99:
    print(f'\nSeu resultado é {Indice_massa_corporal:.2f}, você está com o peso normal, continue assim, {nome}!' )
elif 24.99 <= Indice_massa_corporal < 30:
    print(f'Seu resultado é {Indice_massa_corporal:.2f}, você está acima do peso, precisa se precaver, {nome}!' )
else:
    print(f'Seu resultado é {Indice_massa_corporal:.2f}, você está muito acima do peso, precisa se alimentar melhor e praticar exercícios, {nome}!')



