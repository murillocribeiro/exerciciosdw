familia = {
    "Murillo": (21, "castanho escuro"),
    "Wilson": (52, "preto"),
    "Marineis": (47, "azul"),
    "Pedro Henrique": (7, "verde"),
    "Gabriela": (26, "castanho claro")
}

print("Detalhes dos membros da família:")
for nome, (idade, cor_olhos) in familia.items():
    print(f"Nome: {nome}, Idade: {idade}, Cor dos olhos: {cor_olhos}")
