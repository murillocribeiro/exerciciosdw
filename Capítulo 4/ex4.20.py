from datetime import datetime

data_atual = datetime.now()

data_formatada = data_atual.strftime("%d-%m-%Y")

print("Data atual no formato 'DD-MM-AAAA':", data_formatada)
