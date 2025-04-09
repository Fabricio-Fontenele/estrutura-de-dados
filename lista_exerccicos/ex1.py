# 1. Faca um programa que possua um vetor denominado A que armazene 6 números
# inteiros. O programa deve executar os seguintes passos:
# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
# (b) Armazene em uma variável inteira (simples) a soma entre os valores das
# posições A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
# (c) Modifique o vetor na posic¸a˜o 4, atribuindo a esta posic¸a˜o o valor 100.
# (d) Mostre na tela cada valor do vetor A, um em cada linha.


A = [1, 0, 5, -2, -5, 7]
b = A[0] + A[1] + A[5]

print(b)
print('')

A[4] = 100

for numbers in A:
    print(numbers)