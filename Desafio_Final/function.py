import aiohttp
import sys
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



async def criar_usuario(session: aiohttp.ClientSession) -> Dict[str, str]:
    usuario = criar_dados()
    try:
        async with session.post(URL, json=usuario) as response:
            if response.status == 201:
                print('Usuário criado com sucesso!')
                return usuario
            else:
                print('Erro ao criar usuário:', await response.text())
                sys.exit(1)
    except Exception as err:
        print('Erro inesperado:', err)
        sys.exit(1)
    
    

async def fazer_login(session: aiohttp.ClientSession, usuario: Dict[str, str]) -> Dict:
    dados_login = {
        "email": usuario['email'],
        "password": usuario['password']
    }

    try:
        async with session.post(URL_LOGIN, json=dados_login) as response:
            if response.status == 200:
                print('Login bem-sucedido!')
                return await response.json()
            else:
                print('Erro no login:', await response.text())
                sys.exit(1)
    except Exception as err:
        print('Erro inesperado:', err)
        sys.exit(1)
    
    

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