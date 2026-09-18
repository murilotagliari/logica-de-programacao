# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Murilo Tagliari
# Data: 18/02/26
# Link do Repositório: https://github.com/murilotagliari/logica-de-programacao
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    - Remove espaços extras das pontas.
    - Converte o texto para letras maiúsculas.
    """
    return texto.strip().upper()


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    - Remove espaços das pontas.
    - Utiliza fatiamento [x:y] para extrair os 2 primeiros dígitos.
    """
    dado = dado.strip()
    return dado[0:2]


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    - Percorre a lista usando FOR.
    - Separa os dados usando split(";").
    - Formata nome e cargo usando a Função 1.
    - Extrai o DDD usando a Função 2.
    - Exibe os dados formatados.
    - Retorna a quantidade de registros processados.
    """
    total = 0

    for cadastro in lista_dados:
        partes = cadastro.split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        ddd = extrair_codigo_ou_ddd(partes[2])

        print(f"Nome: {nome} | Cargo: {cargo} | DDD: {ddd}")

        total += 1

    return total


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    dados_brutos = [
        "João da Silva;Analista de Sistemas;11987654321",
        "Maria Oliveira;Gerente;21987654321",
        "Carlos Souza;Desenvolvedor;31987654321"
    ]

    # Chamada da Função 3
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")

if __name__ == "__main__":
    main()
