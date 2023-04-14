while True:
    NomeDeUsuario = input("Digite o nome de usuário: ")
    Senha = input("Digite a senha: ")
    
    if NomeDeUsuario == Senha:
        print("A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Nome de usuário e senha aceitos.")
        break
