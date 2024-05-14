def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 6
resultado = eh_par(numero)
print(f"O número {numero} é par? {resultado}")
