soma_impares = 0

for numero in range(1, 101):
    
    if numero % 2 != 0:
    
        soma_impares += numero
        print(numero, end=" ")

print("\nA soma de todos os números ímpares de 1 a 100 é:", soma_impares)
