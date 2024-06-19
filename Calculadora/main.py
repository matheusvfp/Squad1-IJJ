import op_calculadora as calc

print("Calculadora!!")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = int(input("Selecione a operação: "))
num1 = int(input("Selecione o numero 1: "))
num2 = int(input("Selecione o numero 2: "))
        
resultado = calc.op(operacao,num1,num2)
print(f"O resultado da operação é: {resultado}")