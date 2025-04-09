# 7. Escreva um programa que leia 10 nu´meros inteiros e os armazene em um vetor.
# Imprima o vetor, o maior elemento e a posic¸a˜o que ele se encontra.a

numbers = []
maiores = []
for i in range(1, 10+1):
    number = int(input(f'digite o {i}º termo: '))
    numbers.append(number)

maior = max(numbers)
# index = numbers.index(maior)

for i, v in enumerate(numbers):
    if v == maior:
        maiores.append(i)

print(f'o maior numero digitado foi: {maior}\nna posição {maiores}')