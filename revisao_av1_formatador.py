# ==============================================================================
# REVISAO PARA A AV1: MODULARIZACAO E MANIPULACAO DE STRINGS
# ARQUIVO: revisao_av1_formatador.py
# Nome do Aluno: murilo tagliari
# Data: 25/08
# ==============================================================================

def formatar_citacao(nome_completo):
    partes = nome_completo.split()

    sobrenome = partes[-1].upper()

    nome = " ".join(partes[:-1])

    return sobrenome + ", " + nome


def gerar_codigo(ano, cpf):
    cpf = cpf.strip()

    tres_primeiros_digitos = cpf[:3]

    return "ALU-" + ano + "-" + tres_primeiros_digitos

autor = "Carlos Eduardo Andrade"
citacao_formatada = formatar_citacao(autor)
print("Citacao Bibliografica:", citacao_formatada)

matricula = gerar_codigo("2026", "456.789.123-00")
print("Matricula Gerada     :", matricula)
