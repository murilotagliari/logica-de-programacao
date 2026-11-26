# Sistema de Biblioteca

biblioteca = [
    {"codigo": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"codigo": 2, "titulo": "Harry Potter", "autor": "J.K. Rowling", "ano": 1997},
    {"codigo": 3, "titulo": "O Pequeno Principe", "autor": "Saint-Exupery", "ano": 1943}
]

def cadastrar(lista):
    try:
        codigo = int(input("Código: "))

        for livro in lista:
            if livro["codigo"] == codigo:
                print("Código já existe!")
                return

        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        lista.append({"codigo": codigo, "titulo": titulo, "autor": autor, "ano": ano})
        print("Livro cadastrado!")

    except ValueError:
        print("Digite números válidos!")

def listar(lista):
    if not lista:
        print("Biblioteca vazia!")
    for livro in lista:
        print(livro)

def buscar(lista):
    try:
        codigo = int(input("Digite o código: "))
        for livro in lista:
            if livro["codigo"] == codigo:
                print("Livro encontrado:", livro)
                return
        print("Livro não encontrado!")
    except ValueError:
        print("Código inválido!")

def remover(lista):
    try:
        codigo = int(input("Código para remover: "))
        for i in range(len(lista)):
            if lista[i]["codigo"] == codigo:
                lista.pop(i)
                print("Livro removido!")
                return
        print("Livro não encontrado!")
    except ValueError:
        print("Código inválido!")

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Remover")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar(biblioteca)
    elif opcao == "2":
        listar(biblioteca)
    elif opcao == "3":
        buscar(biblioteca)
    elif opcao == "4":
        remover(biblioteca)
    elif opcao == "5":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")
