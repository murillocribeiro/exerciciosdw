a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação aritmética (+, -, * ou /): ")

match operacao:
    case "+":
        resultado = a + b
        print(f"O resultado da soma é: {resultado}")
    case "-":
        resultado = a - b
        print(f"O resultado da subtração é: {resultado}")
    case "*":
        resultado = a * b
        print(f"O resultado da multiplicação é: {resultado}")
    case "/":
        if b != 0:
            resultado = a / b
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    case _:
        print("Operação aritmética inválida.")
