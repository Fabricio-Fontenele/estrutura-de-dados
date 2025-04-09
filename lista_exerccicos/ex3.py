# Ler um conjunto de números reais, armazenando-o em vetor e calcular o
# quadrado das componentes deste vetor, armazenando o resultado em outro
# vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.

numbers = []
qudrado = []
for i in range(1,6):
    number = int(input(f'digite o {i}º numero: '))
    numbers.append(number)

for number in numbers:
    number = number ** 2
    qudrado.append(number)

print(numbers)
print(qudrado)