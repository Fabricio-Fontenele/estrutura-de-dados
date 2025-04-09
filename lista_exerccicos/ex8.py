# 8. Crie um programa que leˆ 6 valores inteiros e, em seguida, mostre na tela os valores
# lidos na ordem inversa.

values = []

for i in range(1, 6):
    value = int(input('digite o {i}º valor: '))
    values.append(value)

print(values)


print(values[::-1])