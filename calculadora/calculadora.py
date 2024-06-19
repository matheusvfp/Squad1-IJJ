def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculator():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite a escolha (1/2/3/4/5): ")

        match escolha:
            case '1':
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"Resultado: {add(x, y)}")
            case '2':
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"Resultado: {subtract(x, y)}")
            case '3':
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"Resultado: {multiply(x, y)}")
            case '4':
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"Resultado: {divide(x, y)}")
            case '5':
                print("Saindo...")
                break
            case _:
                print("Escolha inválida! Tente novamente.")

if __name__ == "__main__":
    calculator()