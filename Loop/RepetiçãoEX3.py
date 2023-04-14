nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("O nome deve conter mais de 3 caracteres.")
    nome = input("Digite seu nome: ")

idade_str = input("Digite sua idade: ")
while not idade_str.isnumeric() or int(idade_str) < 0 or int(idade_str) > 150:
    print("A idade deve estar entre 0 e 150 anos.")
    idade_str = input("Digite sua idade: ")
idade = int(idade_str)

salario_str = input("Digite seu salário: ")
while not salario_str.replace('.', '', 1).isnumeric() or float(salario_str) <= 0:
    print("O salário deve ser maior que zero.")
    salario_str = input("Digite seu salário: ")
salario = float(salario_str)

genero = input("Digite sua identidade de gênero (Feminino, Masculino ou Indefinido): ")
while genero not in ['Feminino', 'Masculino', 'Indefinido']:
    print("Gênero inválido. Digite 'Feminino' para feminino, 'Masculino' para masculino ou 'Indefinido' para não informado.")
    genero = input("Digite seu gênero (F/M/I): ")

estado_civil = input("Digite seu estado civil: Solteiro(a), Casado(a), Viúvo(a) ou Divorciado(a): ")
while estado_civil not in ['Solteiro', 'Solteira', 'Casado', 'Casada', 'Viúvo', 'Viúva', 'Divorciado', 'Divorciada']:
    print("Estado civil inválido. Digite 'Solteiro' para solteiro(a), 'Casado' para casado(a), 'Vivo' para viúvo(a) ou 'Divorciado' para divorciado(a).")
    estado_civil = input("Digite seu estado civil (S/C/V/D): ")

sexualidade = input("Digite sua sexualidade: Hétero, Gay, Lésbica, Bissexual, Pansexual ou Outro: ")
while sexualidade not in ['Hétero', 'Gay', 'Lésbica', 'Bissexual', 'Pansexual', 'Outro']:
    print("Sexualidade inválida, Digite 'Hétero' para Hétero, 'Gay' para Gay, 'Lésbica' para Lésbica, 'Bissexual' para Bissexual, 'Pansexual' para Pansexual e 'Outro' para Outro ")
    sexualidade = input("Digite sua sexualidade (H/G/L/B/P/O): ")

print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Identidade de gênero: {genero}")
print(f"Estado Civil: {estado_civil}")
print(f"Sexualidade: {sexualidade}")
print("Muito obrigado por participar!")
