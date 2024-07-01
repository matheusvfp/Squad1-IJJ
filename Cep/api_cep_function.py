import requests as res

integrantes = {
    "integrante_1" : {
        "nome" : "Matheus",
        "cep" : "59900000"
    },
    "integrante_2" : {
        "nome" : "Edson",
        "cep" : "01153000"
    },
    "integrante_3" : {
        "nome" : "Marcus",
        "cep" : "59900000"
    },
    "integrante_4" : {
        "nome" : "Yuri",
        "cep" : "59900000"
    },
    "integrante_5" : {
        "nome" : "Joyce Mayara",
        "cep" : "01153000"
    },
    "integrante_6" : {
        "nome" : "Larissa",
        "cep" : "60015000"
    }

}

def consuta_cep (cep):
    response  = res.get(f"https://viacep.com.br/ws/{cep}/json/")
    if (response.status_code == 200):
        data = response.json()
        return data["localidade"]
    else:
       return {
          "erro": f"Erro na execução: {response.status_code}",
             "status_codes": {
                    "1xx": "Informativo: Informação recebida e processamento continua.",
                    "3xx": "Redirecionamento: Ação adicional necessária para completar a requisição.",
                    "4xx": "Erro do Cliente: Requisição possui erro ou não pode ser completada.",
                    "5xx": "Erro do Servidor: Servidor encontrou um erro ao tentar completar a requisição."
                }
            }

def exibir(integrantes):
    for chave, valor in integrantes.items():
        nome = valor["nome"]
        cidade = consuta_cep(valor["cep"])
        print(f"Nome: {nome}, cidade: {cidade}")
        

 