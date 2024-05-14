import math
import locale

def calcular_raiz_quadrada(numero):
    return math.sqrt(numero)

def formatar_valor_monetario(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)

def main():
    try:
        numero = float(input("Digite um número: "))
        raiz_quadrada = calcular_raiz_quadrada(numero)
        raiz_formatada = formatar_valor_monetario(raiz_quadrada)
        print("A raiz quadrada de {} é {}".format(numero, raiz_formatada))
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
