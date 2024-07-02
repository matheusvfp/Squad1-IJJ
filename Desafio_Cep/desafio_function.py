import requests

def verificar_cidade (cep):
    response  = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if (response.status_code == 200):
        data = response.json()
        return data["localidade"]
    else: 
        return False
    

def verificar_frete_gratis_norte_nordeste(cep):
    
    estados_frete_gratis = {
    'Acre': {'inicio': '69', 'fim': '69'},
    'Alagoas': {'inicio': '57', 'fim': '57'},
    'Amazonas': {'inicio': '69', 'fim': '69'},
    'Amapá': {'inicio': '68', 'fim': '68'},
    'Bahia': {'inicio': '40', 'fim': '48'},
    'Ceará': {'inicio': '60', 'fim': '62'},
    'Maranhão': {'inicio': '65', 'fim': '67'},
    'Pará': {'inicio': '66', 'fim': '67'},
    'Paraíba': {'inicio': '58', 'fim': '58'},
    'Pernambuco': {'inicio': '50', 'fim': '56'},
    'Piauí': {'inicio': '64', 'fim': '64'},
    'Rio Grande do Norte': {'inicio': '59', 'fim': '59'},
    'Rondônia': {'inicio': '76', 'fim': '76'},
    'Roraima': {'inicio': '69', 'fim': '69'},
    'Sergipe': {'inicio': '49', 'fim': '49'},
    'Tocantins': {'inicio': '77', 'fim': '77'}
}

    estado_usuario = cep[:2]
    

    for estado_frete, valor in estados_frete_gratis.items():
        inicio_intervalo = valor['inicio']
        fim_intervalo = valor['fim']
        
        if inicio_intervalo <= estado_usuario <= fim_intervalo:
            cidade = verificar_cidade(cep)
            if cidade != False:
                print(f"A cidade de {cidade} do estado {estado_frete} com o CEP {cep}  possui FRETE GRÁTIS!")
            else:
                print(f"o CEP {cep} do estado {estado_frete} possui FRETE GRÁTIS!")
            return True

    print(f"O estado correspondente ao CEP {cep} não possui frete grátis.")
    return False


