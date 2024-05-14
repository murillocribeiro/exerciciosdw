def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero!"

while True:
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite números válidos!")
            continue

        if escolha == '1':
            print("Resultado da soma:", soma(num1, num2))
        elif escolha == '2':
            print("Resultado da subtração:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado da multiplicação:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado da divisão:", divisao(num1, num2))
    elif escolha == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
