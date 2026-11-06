cadastros = [
    {"nome": "Ana Silva", "idade": 17, "curso": "Informática"},
    {"nome": "João Santos", "idade": 18, "curso": "Administração"}
]

print("=== Cadastro de Novo Aluno ===")

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")

novo_aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

cadastros.append(novo_aluno)

print("\n=== Lista de Alunos Cadastrados ===")

for aluno in cadastros:
    print("----------------------------")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])# 1. Criar a base inicial de cadastros
cadastros = [
    {"nome": "Ana Silva", "idade": 17, "curso": "Informática"},
    {"nome": "João Santos", "idade": 18, "curso": "Administração"}
]

print("=== Cadastro de Novo Aluno ===")

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")

novo_aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

cadastros.append(novo_aluno)

print("\n=== Lista de Alunos Cadastrados ===")

for aluno in cadastros:
    print("----------------------------")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Curso:", aluno["curso"])
