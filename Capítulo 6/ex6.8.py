numeros_str = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros_str.split()))

quadrados = list(map(lambda x: x**2, numeros))

print("Quadrados dos números:", quadrados)
