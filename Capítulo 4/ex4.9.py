import re

cpf = input("Digite um CPF (no formato DDD.DDD.DDD-DD): ")

padrao_cpf = r"\d{3}\.\d{3}\.\d{3}-\d{2}"

if re.fullmatch(padrao_cpf, cpf):
    print("CPF válido!")
else:
    print("CPF inválido. Por favor, digite um CPF no formato correto.")
