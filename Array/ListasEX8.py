idadesalocada = []
alturasalocada = []

for i in range(5):
    idade = int(input("Digite a idade da pessoa de número {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa de número {}: ".format(i+1)))
    idadesalocada.append(idade)
    alturasalocada.append(altura)

print("\nIdades na ordem inversa do alocado:")
for idade in reversed(idadesalocada):
    print(idade)

print("\nAlturas na ordem inversa do alocado:")
for altura in reversed(alturasalocada):
    print(altura)
