numeros = [32, 431, 532, 654, 412]
indice = 0
maior_numero = numeros[indice]

while indice < len(numeros):
    if numeros[indice] > maior_numero:
        maior_numero = numeros[indice]
    indice += 1

print(maior_numero)

