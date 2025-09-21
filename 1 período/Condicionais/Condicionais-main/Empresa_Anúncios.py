def formatar_midia(midia):
    midia_lower = midia.lower()
    if midia_lower in {'rádio', '1'}:
        return 1
    elif midia_lower in {'tv', '2'}:
        return 2
    elif midia_lower in {'revista', '3'}:
        return 3
    elif midia_lower in {'outdoor', '4'}:
        return 4
    else:
        return None
total_receber = 0
total_anuncios = {1: 0, 2: 0, 3: 0, 4: 0}

for _ in range(7):
    tipo_midia = formatar_midia(input("Digite o tipo de mídia utilizando o nome, ou digite suas numerações (Rádio (1), TV(2), Revista(3), Outdoor(4)): "))
    if tipo_midia == 1:
        faixa = int(input("Digite a faixa (1-AM, 2-FM): "))
        if faixa == 1:
            total_receber += 300
        elif faixa == 2:
            total_receber += 500
        total_anuncios[1] += 1

    elif tipo_midia == 2:
        horario = int(input("Digite o horário (valor inteiro): "))
        if horario > 20:
            total_receber += 2000
        else:
            total_receber += 1200
        total_anuncios[2] += 1

    elif tipo_midia == 3:
        total_receber += 750
        total_anuncios[3] += 1

    elif tipo_midia == 4:
        total_receber += 1500
        total_anuncios[4] += 1

print(f"\nTotal a ser recebido pela empresa: R$ {total_receber:.2f}")
print("Quantidade de anúncios por mídia:")
for tipo, quantidade in total_anuncios.items():
    print(f"{tipo}: {quantidade}")
