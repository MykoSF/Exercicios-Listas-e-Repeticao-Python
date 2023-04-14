PrimeiroNumero = int(input("Digite o primeiro número natural: "))
SegundoNumero = int(input("Digite o segundo número natural: "))

menor = min(PrimeiroNumero, SegundoNumero)
maior = max(PrimeiroNumero, SegundoNumero)

for i in range(menor, maior + 1):
    print(i)
