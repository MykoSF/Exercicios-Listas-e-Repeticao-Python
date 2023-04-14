palavra = ["f", "i", "n", "a", "l", "i", "d", "a", "d", "e"]
quantidadeconsoantes = 0

for letrasconsoante in palavra:
    if letrasconsoante not in "aeiou":
        quantidadeconsoantes = quantidadeconsoantes + 1
        print(letrasconsoante)

print("A quantidade de letras consoantes é de: " + str(quantidadeconsoantes))
