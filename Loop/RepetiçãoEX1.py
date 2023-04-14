while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        print("Nota válida informada:", nota)
    else:
        print("Valor inválido, A nota precisa estar entre 0 e 10.")
        break


