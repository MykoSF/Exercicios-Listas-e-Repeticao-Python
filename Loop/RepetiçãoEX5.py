def main():
    while True:
        calcular_crescimento_populacional()
        resposta = input("Deseja recalcular os dados? (s/n): ")
        if resposta.lower() != "s":
            break

def calcular_crescimento_populacional():   
    populacao_a = 0
    populacao_b = 0
    taxa_crescimento_a = 0
    taxa_crescimento_b = 0

    while populacao_a <= 0:
        populacao_a = int(input("Informe a população inicial do país A: "))
        if populacao_a <= 0:
            print("Entrada inválida. Digite apenas números maiores que zero para a população do país A.")
    while taxa_crescimento_a <= 0:
        taxa_crescimento_a = float(
            input("Informe a taxa de crescimento anual do país A (em decimal): "))
        if taxa_crescimento_a <= 0:
            print("Entrada inválida. Digite apenas números maiores que zero para a taxa de crescimento do país A.")
    while populacao_b <= 0:
        populacao_b = int(input("Informe a população inicial do país B: "))
        if populacao_b <= 0:
            print("Entrada inválida. Digite apenas números maiores que zero para a população do país B.")
    while taxa_crescimento_b <= 0:
        taxa_crescimento_b = float(
            input("Informe a taxa de crescimento anual do país B (em decimal): "))
        if taxa_crescimento_b <= 0:
            print("Entrada inválida. Digite apenas números maiores que zero para a taxa de crescimento do país B.")

    anos = 0

    while populacao_a < populacao_b:
        populacao_a *= 1 + taxa_crescimento_a
        populacao_b *= 1 + taxa_crescimento_b
        anos += 1

    print("A população do país A ultrapassará a população do país B em", anos, "anos.")
