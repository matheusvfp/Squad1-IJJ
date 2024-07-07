import requests
from faker import Faker
from typing import Dict, Union
import pandas as pd

URL = 'https://desafiopython.jogajuntoinstituto.org/api/users/'
URL_LOGIN = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'

def criar_dados() -> Dict[str,str]:
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


def criar_usuario() -> Union[Dict[str, str], None]:
    usuario = criar_dados()
    response = requests.post(URL, json=usuario)
    
    if response.status_code == 201: 
        print('Usuário criado com sucesso!')
        return usuario  
    else:
        print('Erro ao criar usuário:', response.text)
        return None
    
def fazer_login(usuario: Dict[str,str]) -> Union[Dict, None]:
    dados_login = {
        "email": usuario['email'],
        "password": usuario['password']
    }

    response = requests.post(URL_LOGIN, json=dados_login)

    if response.status_code == 200:  
        print('Login bem-sucedido!')
        token_acesso = response.json()
        return token_acesso
    else:
        print('Erro no login:', response.text)
        return None
    
 
def gerar_dataframe(retorno: Dict[str, str]) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(retorno, orient='index')
    return df