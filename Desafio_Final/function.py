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
        response.raise_for_status()
        if response.status_code == 201:
            print('Usuário criado com sucesso!')
            salvar_json('usuario_criado.json', usuario)
            return usuario
        else:
            raise RuntimeError(f'Erro ao criar usuário: {response.text}')
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f'Erro inesperado: {err}')
    
    

def fazer_login(session: requests.Session, usuario: Dict[str, str]) -> Dict:
    dados_login = {
        "email": usuario['email'],
        "password": usuario['password']
    }

    try:
        response = session.post(URL_LOGIN, json=dados_login)
        response.raise_for_status()
        if response.status_code == 200:
            print('Login bem-sucedido!')
            token_acesso = response.json()
            salvar_json('token_acesso.json', token_acesso)
            return token_acesso
        else:
            raise RuntimeError(f'Erro no login: {response.text}')
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f'Erro inesperado: {err}')
    
    

def salvar_json(nome_arquivo: str, dados: Dict) -> None:
    try:
        with open(nome_arquivo, "w") as save_file:
            json.dump(dados, save_file, indent=6)
    except Exception as err:
        raise RuntimeError(f'Erro ao salvar JSON em {nome_arquivo}: {err}')
    
    

def gerar_dataframe(retorno: Union[Dict[str, str], None]) -> pd.DataFrame:
    if retorno is None:
        raise ValueError('Erro: Dados de retorno são None')
    
    try:
        df = pd.DataFrame([retorno])
        return df
    except Exception as err:
        raise RuntimeError(f'Erro ao criar DataFrame: {err}')
    
    

def salvar_em_csv(df: pd.DataFrame, nome_do_arquivo: str) -> None:
    try:
        df.to_csv(nome_do_arquivo, index=False)
    except Exception as err:
        raise RuntimeError(f'Erro ao salvar CSV: {err}')
