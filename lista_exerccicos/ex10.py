# 10. Fac¸a um programa para ler a nota da prova de 15 alunos e armazene num vetor,
# calcule e imprima a me´dia geral.

notas = []

for i in range(0,15):
    nota = float(input(f'Digite a nota do {i}º aluno'))
    notas.append(nota)

print(f'a media geral das notas foi {sum(notas) / len(notas)}')