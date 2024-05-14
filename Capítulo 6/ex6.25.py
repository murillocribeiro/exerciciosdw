import random

pessoas = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"]

amigo_secreto = {}

while len(pessoas) > 1:
    pessoa = random.choice(pessoas)
    amigo = random.choice([p for p in pessoas if p != pessoa])
    amigo_secreto[pessoa] = amigo
    pessoas.remove(amigo)
    pessoas.remove(pessoa)

if pessoas:
    amigo_secreto[pessoas[0]] = random.choice([p for p in amigo_secreto.keys() if p != pessoas[0]])

for pessoa, amigo in amigo_secreto.items():
    print(f"{pessoa} tirou {amigo} no amigo secreto.")
