# 2. Crie um programa que leˆ 6 valores inteiros e, em seguida, mostre na tela os
# valores lidos.

numbers = []

for i in range(1,6):
    number = int(input('digite um numero: '))
    numbers.append(number)

print(numbers)