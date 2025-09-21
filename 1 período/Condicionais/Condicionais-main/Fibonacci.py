N = int(input("Digite um inteiro N (N < 46): "))
if N >= 46:
    print("Por favor, digite um valor menor que 46.")
else:
    s0, s1 = 0, 1

    print(f"Os primeiros {N} termos da série de Fibonacci são:")
    print(s0, end=" ")
    print(s1, end=" ")

    for _ in range(2, N):
        proximo_termo = s0 + s1
        print(proximo_termo, end=" ")
        s0, s1 = s1, proximo_termo

