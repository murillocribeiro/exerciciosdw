nome = input("Digite o nome da pessoa: ")
salario_bruto = float(input("Digite o salário bruto da pessoa: "))
imposto = float(input("Digite o valor do imposto da pessoa: "))

salario_liquido = salario_bruto - imposto

print(f"{nome} tem um salário líquido de R$ {salario_liquido:.2f}.")
