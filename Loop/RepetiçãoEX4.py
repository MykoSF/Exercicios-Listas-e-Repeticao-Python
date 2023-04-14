PopulacaoPais_A = 80000
TaxaPais_A = 0.03

PopulacaoPais_B = 200000
TaxaPais_B = 0.015

anos = 0

while PopulacaoPais_A < PopulacaoPais_B:
    anos += 1
    PopulacaoPais_A *= 1 + TaxaPais_A
    PopulacaoPais_B *= 1 + TaxaPais_B

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a população do país B")
