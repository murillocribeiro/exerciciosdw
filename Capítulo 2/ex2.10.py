temperatura = float(input("Digite sua tempetura: "))

if temperatura > 37:
    print("Sua temperatura está acima do normal, vá ao médico!")

elif temperatura < 36:
    print("Sua temperatura está abaixo do normal, vá ao médico!")

else:
    print("Sua temperatura está normal!")