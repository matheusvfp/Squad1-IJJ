import aiohttp
from faker import Faker
from typing import Dict, Union
import pandas as pd


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

async def criar_usuario(session: aiohttp.ClientSession) -> Union[Dict[str, str], None]:
    usuario = criar_dados()
    try:
        async with session.post(URL, json=usuario) as response:
            if response.status == 201:
                print('Usuário criado com sucesso!')
                return usuario
            else:
                print('Erro ao criar usuário:', await response.text())
    except Exception as err:
        print('Erro inesperado:', err)
    return None

async def fazer_login(session: aiohttp.ClientSession, usuario: Dict[str, str]) -> Union[Dict, None]:
    dados_login = {
        "email": usuario['email'],
        "password": usuario['password']
    }

    try:
        async with session.post(URL_LOGIN, json=dados_login) as response:
            if response.status == 200:
                print('Login bem-sucedido!')
                token_acesso = await response.json()
                return token_acesso
            else:
                print('Erro no login:', await response.text())
    except Exception as err:
        print('Erro inesperado:', err)
    return None

def gerar_dataframe(retorno: Union[Dict[str, str], None]) -> Union[pd.DataFrame, None]:
    if retorno is None:
        print('Erro: Dados de retorno são None')
        return None
    try:
        df = pd.DataFrame([retorno])
        print(df)
        return df
    except Exception as err:
        print('Erro ao criar DataFrame:', err)
        return None



