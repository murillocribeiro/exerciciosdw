from datetime import datetime, timedelta

hora_atual = datetime.now()

nova_hora = hora_atual - timedelta(hours=2)

print("Hora atual menos 2 horas:", nova_hora.time())
