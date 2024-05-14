def transformarLista(lista, funcao):
    return [funcao(numero) for numero in lista]

def porExtenso(numero):
    numeros_por_extenso = {
        0: "zero",
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove"
    }
    return numeros_por_extenso[numero]

lista_transformada = transformarLista([1, 2, 3, 4, 5], porExtenso)

print(lista_transformada)
