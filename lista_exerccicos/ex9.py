# 9. Crie um programa que leˆ 6 valores inteiros pares e, em seguida, mostre na tela os
# valores lidos na ordem inversa.

numbers = []

while True:
    value = int(input('Digite um valor: '))
    if value != 0:
        if value % 2 == 0:
            numbers.append(value)
    if len(numbers) == 6:
        break

print(numbers)


print(numbers[::-1])