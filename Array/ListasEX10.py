PrimeiraLista = [12, 321, 431, 356, 421, 76, 512, 55, 632, 545, ]
SegundaLista = [754, 345, 654, 65, 47, 9, 69, 765, 5356, 395]
ListaConjunta = [0] * 20

for i in range(10):
    ListaConjunta[i*2] = PrimeiraLista[i]
    ListaConjunta[i*2+1] = SegundaLista[i]

print("Lista número 1: ", PrimeiraLista)
print("Lista número 2: ", SegundaLista)
print("Lista conjunta: ", ListaConjunta)
