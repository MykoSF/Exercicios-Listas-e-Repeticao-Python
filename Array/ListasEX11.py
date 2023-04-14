PrimeiraLista = [12, 321, 431, 356, 421, 76, 512, 55, 632, 545]
SegundaLista = [754, 345, 654, 65, 47, 9, 69, 765, 5356, 395]
TerceiraLista = [23, 54, 64, 789, 23, 43, 12, 76, 54, 324]
ListaConjunta = [0] * 30

for i in range(10):
    ListaConjunta[i*3] = PrimeiraLista[i]
    ListaConjunta[i*3+1] = SegundaLista[i]
    ListaConjunta[i*3+2] = TerceiraLista[i]

print("Lista número 1: ", PrimeiraLista)
print("Lista número 2: ", SegundaLista)
print("Lista número 3: ", TerceiraLista)
print("Lista conjunta: ", ListaConjunta)
