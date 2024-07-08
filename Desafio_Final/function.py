import sys
from faker import Faker
from typing import Dict, Union
import pandas as pd
import json
import requests


URL = 'https://desafiopython.jogajuntoinstituto.org/api/users/'
URL_LOGIN = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'



def criar_dados() -> Dict[str, str]:
    faker = Faker('pt_BR')
    usuario = {
        "username": faker.user_name(),
        "email": faker.free_email(),
        "password": faker.password(),
        "phone": faker.phone_number()[:14],
        "address": faker.address(),
        "cpf": faker.cpf()
    }
    return usuario



def criar_usuario(session: requests.Session) -> Dict[str, str]:
    usuario = criar_dados()
    try:
        response = session.post(URL, json=usuario)
        if response.status_code == 201:
            print('Usuário criado com sucesso!')
            salvar_json('usuario_criado.json', usuario)
            return usuario
        else:
            print('Erro ao criar usuário:', response.text)
            sys.exit(1)
    except Exception as err:
        print('Erro inesperado:', err)
        sys.exit(1)


def fazer_login(session: requests.Session, usuario: Dict[str, str]) -> Dict:
    dados_login = {
        "email": usuario['email'],
        "password": usuario['password']
    }

    try:
        response = session.post(URL_LOGIN, json=dados_login)
        if response.status_code == 200:
            print('Login bem-sucedido!')
            token_acesso = response.json()
            salvar_json('token_acesso.json', token_acesso)
            return token_acesso
        else:
            print('Erro no login:', response.text)
            sys.exit(1)
    except Exception as err:
        print('Erro inesperado:', err)
        sys.exit(1)


def salvar_json(nome_arquivo: str, dados: Dict) -> None:
    try:
        with open(nome_arquivo, "w") as save_file:
            json.dump(dados, save_file, indent=6)
    except Exception as err:
        print(f'Erro ao salvar JSON em {nome_arquivo}:', err)
        

def gerar_dataframe(retorno: Union[Dict[str, str], None]) -> pd.DataFrame:
    if retorno is None:
        sys.exit('Erro: Dados de retorno são None')
    
    try:
        df = pd.DataFrame([retorno])
        return df
    except Exception as err:
        print('Erro ao criar DataFrame:', err)
        sys.exit(1)


def salvar_em_csv(df: pd.DataFrame, nome_do_arquivo: str) -> None:
    df.to_csv(nome_do_arquivo, index=False)
    
