# Fac¸a um programa que preencha um vetor com 10 nu´meros reais, calcule e
#mostre a quantidade de nu´meros negativos e a soma dos nu´meros positivos
#desse vetor.

numbers = list(map(int, input('digite 10 valors: ').split()))[:10]

negativos = []
positivos = []
for n in numbers:
    if n < 0:
        negativos.append(n)

for n in numbers:
    if n >= 0:
        positivos.append(n)

print(f'os numeros negativos digitados foram {negativos}')

print(f'a soma dos numeros negativos: = {sum(negativos)}')

print(positivos)
print(f'a soma dos numeros positivos: = {sum(positivos)}')