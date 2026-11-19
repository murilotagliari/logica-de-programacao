numeros = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 81, 89, 94, 99]
busca = int(input("Digite o número inteiro que deseja procurar: "))

inicio = 0
fim = len(numeros) - 1
comparacoes = 0
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes += 1
    if numeros[meio] == busca:
        posicao = meio
        break
    elif busca > numeros[meio]:
        inicio = meio + 1
    else:
        fim = meio - 1
if posicao != -1:
    print(f"\nNúmero {busca} encontrado!")
    print(f"Índice (posição) na lista: {posicao}")
else:
    print(f"\nNúmero {busca} não foi encontrado na lista.")

print(f"Total de comparações realizadas: {comparacoes}")
