cpf = input("Digite o número do CPF (apenas números): ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido.")
