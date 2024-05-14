import os
import zipfile

os.makedirs("Textos", exist_ok=True)

for i in range(1, 4):
    with open(f"Textos/arquivo{i}.txt", "w") as f:
        f.write("Lista de Exercicios de Python do Ricardo Marochio")

with zipfile.ZipFile("Textos.zip", "w") as zipf:
    for foldername, subfolders, filenames in os.walk("Textos"):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zipf.write(filepath, os.path.relpath(filepath, "Textos"))
