produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}

print("Dicionário do produto:")
print(produto)
print("\nNome do produto:", produto["nome"])
print("Preço do produto:", produto["preco"])

produto["preco"] = 220.0
produto["estoque"] += 6
produto["categoria"] = "Periféricos"

print("\nProduto atualizado:")
print(produto)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}

print("\nChaves do usuário:")
print(usuario.keys())
print("\nValores do usuário:")
print(usuario.values())
