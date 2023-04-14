NotaAlunos = [['Ian', [3, 7, 2, 1]], ['Davi', [7, 7, 5, 1]], ['Cauan', [6, 6, 6, 10]], ['Henrique', [10, 8, 7, 4]], ['Miguel', [9, 8, 10, 2]], ['Maykon', [2, 7, 8, 9]], ['Leticia', [10, 10, 9, 10]], ['Natália', [3, 6, 4, 1]], ['Lorena', [2, 4, 5, 3]], ['Farias', [1, 8, 9, 9]]]
contador_alunos = 0

for aluno in NotaAlunos:
    notas = aluno[1]
    media = sum(notas) / len(notas)
    if media >= 7.00:
        contador_alunos += 1
        print(f"A média das notas de {aluno[0]} é {media:.2f}")

print(f"A quantidade de alunos com média positiva é: {contador_alunos}")
