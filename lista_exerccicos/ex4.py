# 4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
# dois valores X e Y quaisquer correspondentes a duas posic¸o˜es no vetor. Ao final
# seu programa devera´ escrever a soma dos valores encontrados nas respectivas
# posic¸o˜es X e Y .

numbers = list(map(int, input('digite um numero: ').split()))[:8]

print(numbers)
x = int(input('digite a posição x: '))
y = int(input('digite a posição y: '))
print(numbers)
print(f'a soma das posições {x} e {y} e: {numbers[x] + numbers[y]} ')
