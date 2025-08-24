#ciclistas compiten en carrera 
velocidad_1 = int(input("a cuanta velocidad va el 1 "))
velocidad_2 = int(input("a cuanta velocidad va el 2 "))

if velocidad_1 > velocidad_2:
    print("felicidades esres el mas rapido ")
elif velocidad_1 == velocidad_2:
    print("van empates")
else:
    print("lo siento eres lento como tortuga")