try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")

except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: entrada inválida! Certifique-se de digitar números inteiros.")
