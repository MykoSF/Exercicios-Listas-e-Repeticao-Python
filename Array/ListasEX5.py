Todososnúmeros = []
ArrayPar = []
ArrayÍmpar = []

for i in range(1, 21):
    Todososnúmeros.append(i)
    if i % 2 == 0:
        ArrayPar.append(i)
    else:
        ArrayÍmpar.append(i)

print("Todos os de 1 a 20 são: ", Todososnúmeros)
print("Todos os números pares de 1 a 20 são: ", ArrayPar)
print("Todos os ímpares pares de 1 a 20 são: ", ArrayÍmpar)