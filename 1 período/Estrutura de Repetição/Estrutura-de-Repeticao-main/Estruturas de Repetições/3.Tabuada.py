'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada 
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.'''

somar = int(input('Digite um valor inteiro que você deseja tabuar:'))
começo = int(input('digite um valor inteiro pelo qual a tabuada começará:'))
final = int(input('Digite um valor inteiro pelo qual a tabuada finalizará:'))

if final< começo:
    print('O valor final não pode ser menor que o valor inicial.')
else:
    tabuada  = []
    for i in range(começo, final+1):
        tabuada.append(somar*i)

for i in range(len(tabuada)):
    print(f'{somar}X{começo+i} = {tabuada[i]}')