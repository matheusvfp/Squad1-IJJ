import os_function as func

dados = func.definir_dados()

func.criar_pasta(dados[1], dados[2])

arquivo_txt = func.os.path.join(dados[2], "dados.txt")

func.salvar_dados_em_txt(dados[0],arquivo_txt)


