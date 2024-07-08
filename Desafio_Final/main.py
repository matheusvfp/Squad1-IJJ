import function as func
import requests

def main():
    with requests.Session() as session:
        usuario_criado = func.criar_usuario(session)
        token_acesso = func.fazer_login(session, usuario_criado)
        func.gerar_dataframe(token_acesso)



if __name__ == "__main__":
    main()