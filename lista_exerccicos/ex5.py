# 5. Leia um vetor de 10 posic¸o˜es. Contar e escrever quantos valores pares ele
# possui.

numbers = list(map(int, input('Digite 10 numeros: ').split()))[:10]
pares = []

for number in numbers:
    if number % 2 == 0:
        pares.append(number)

print(pares)
print(f'a quantidade de elementos pares que voce digitou é igual a {len(pares)}')