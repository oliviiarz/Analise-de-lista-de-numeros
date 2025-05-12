def analisar_numeros(numeros):
    total = 0
    maior = numeros[0]
    menor = numeros[0]
    pares = 0

    for num in numeros:
        total += num  # Soma dos elementos
        if num > maior:
            maior = num  # o maior número
        if num < menor:
            menor = num  # o menor número
        if num % 2 == 0:
            pares += 1  # Conta números pares

    media = total / len(numeros)
    return media, maior, menor, pares
