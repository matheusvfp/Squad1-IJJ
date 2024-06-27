def contar_vogais(palavra):
    vogais = "AEIOU"
    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador += 1  
    return contador
