import functions as func

usuario = func.criar_usuario()

retorno = func.fazer_login(usuario)

df_retorno = func.gerar_dataframe(retorno)

print(df_retorno)