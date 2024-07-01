import os

def definir_dados():
    linguaguens_programacao = ['C#', 'Java', 'Python', 'JavaScript']
    nome_pasta = "linguagens_de_programação"
    caminho_pasta = "./" + nome_pasta
    return linguaguens_programacao, nome_pasta, caminho_pasta


def criar_pasta(nome_pasta, caminho_pasta):
    
    if os.path.exists(caminho_pasta):
        print(f"Pasta '{nome_pasta}' já existe.")
    else:
        os.makedirs(caminho_pasta)
        print(f"Pasta '{nome_pasta}' criada com sucesso!")


def salvar_dados_em_txt(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for linha in dados:
            arquivo.write(linha + "\n")
    
    print(f"Dados salvos em '{nome_arquivo}'")

