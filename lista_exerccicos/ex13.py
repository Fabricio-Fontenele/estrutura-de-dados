# 13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posic¸a˜o onde se
# encontram o maior e o menor valor.

numbers = list(map(int, input('digite 5 valores: ').split()))[:5]

menor_index = []
maior_index = []

maior = max(numbers)
menor = min(numbers)
for i, v in enumerate(numbers):
    if v == maior:
        maior_index.append(i)

for i, v in enumerate(numbers):
    if v == menor:
        menor_index.append(i)


print(f'o maior numero apareceu na posição {maior_index}')
print(f'o menor valor apareceu em {menor_index}')
