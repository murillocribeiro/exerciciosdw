def decifrar_mensagem(codificada):
    if not codificada:
        return ""

    char = codificada[0].lower()

    if char == 'z':
        return 'a' + decifrar_mensagem(codificada[1:])
    elif 'a' <= char < 'z':
        proximo_char = chr(ord(char) + 1)
        return proximo_char + decifrar_mensagem(codificada[1:])
    else:
        return char + decifrar_mensagem(codificada[1:])

mensagem_codificada = "bcd efgh"
mensagem_decodificada = decifrar_mensagem(mensagem_codificada)
print("Mensagem decodificada:", mensagem_decodificada)
