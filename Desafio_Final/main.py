import function as func
import requests

def main():
    with requests.Session() as session:
        usuario_criado = func.criar_usuario(session)
        token_acesso = func.fazer_login(session, usuario_criado)
        df = func.gerar_dataframe(token_acesso)
        print(df)

if __name__ == "__main__":
    main()