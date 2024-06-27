def contar_vogais(palavra):
    # Lista de vogais
    vogais = "aeiouAEIOU"
    # Contador de vogais
    contador = 0
    
    # Loop para percorrer cada caractere na palavra
    for letra in palavra:
        if letra in vogais:
            contador += 1
    
    return contador

# Solicitar entrada do usuário
palavra = input("Digite uma palavra: ")

# Chamar a função e imprimir o resultado
total_vogais = contar_vogais(palavra)
print(f"O número total de vogais na palavra '{palavra}' é: {total_vogais}")