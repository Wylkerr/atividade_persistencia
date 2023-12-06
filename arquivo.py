def cadastrar_usuario():
    while True:
        nome = input("Digite seu nome (ou '0' para sair): ")
        if nome == '0':
            break

        idade = input("Digite sua idade: ")
        sexo = input("Digite seu sexo (M ou F): ")
        telefone = input("Digite seu telefone: ")

        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

        print("Usuário cadastrado!\n")

if __name__ == "__main__":
    print("Bem-vindo ao formulário de cadastro!")
    cadastrar_usuario()