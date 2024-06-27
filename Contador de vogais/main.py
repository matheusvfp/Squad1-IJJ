import func_vogais as func

palavra = str(input("Digite uma palavra: "))
texto_maiusculas = palavra.upper()
print(f"Número de vogais: {func.contar_vogais(texto_maiusculas)}")