# 12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores 
# lidos juntamente com o maior, o menor e a média dos valores.

numbers = list(map(int, input('Digite 5 valores: ').split()))[:5]

print(f'os valores digitados foram {numbers}')

print(f'o maior foi: {max(numbers)}')
print(f'o menos foi: {min(numbers)}')
print(f'a media dos valores foi: {sum(numbers) / len(numbers):f.2}')