def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y



def op(operacao, num1, num2):
    match operacao:
        case 1:
            return add(num1, num2)
        case 2:
            return sub(num1, num2)
        case 3:
            return mult(num1, num2)
        case 4:
            return div(num1, num2)
        case _:
            return "Operação inválida!"