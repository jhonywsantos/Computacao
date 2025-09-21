def calcular_percentuais(quantidade_ratos, quantidade_coelhos, quantidade_sapos):
    total_cobaias = quantidade_ratos + quantidade_coelhos + quantidade_sapos
    percentual_ratos = (quantidade_ratos / total_cobaias) * 100
    percentual_coelhos = (quantidade_coelhos / total_cobaias) * 100
    percentual_sapos = (quantidade_sapos / total_cobaias) * 100
    return total_cobaias, percentual_ratos, percentual_coelhos, percentual_sapos

quantidade_testes = int(input("Digite a quantidade de testes: "))

total_ratos = 0
total_coelhos = 0
total_sapos = 0

for _ in range(quantidade_testes):
    quantidade_ratos = int(input("Digite a quantidade de ratos: "))
    quantidade_coelhos = int(input("Digite a quantidade de coelhos: "))
    quantidade_sapos = int(input("Digite a quantidade de sapos: "))

    total_ratos += quantidade_ratos
    total_coelhos += quantidade_coelhos
    total_sapos += quantidade_sapos

total_cobaias, percentual_ratos, percentual_coelhos, percentual_sapos = calcular_percentuais(total_ratos, total_coelhos, total_sapos)

print(f'A quantidade total de testes foram: {quantidade_testes}')
print(f"Total de cobaias em todos os testes: {total_cobaias}")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
