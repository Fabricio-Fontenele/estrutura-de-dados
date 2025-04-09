# 6. Fac¸a um programa que receba do usua´rio um vetor com 10 posic¸o˜es. Em seguida
# devera´ ser impresso o maior e o menor elemento do vetor.

numbers = list(map(int, input("digite 10 valores: ").split()))[:10]

print(numbers)

print(f'o menor numero digitado foi:{min(numbers)}')
print(f'o maior numero digitado foi: {max(numbers)}')
