#def adivina_el_numero(x):

print("===============================================================")
print(" ¡Bienvenido al juego!")
print("===============================================================")
print("Tu meta es adivinar el numero generado por la computadora.")

numero_aleatorio = random.randint(1,x)

prediccion = 0

while prediccion !=numero_aleatorio:
    #El usurio ingresa un numero 
        prediccion = int(input(f"adivina un numero entre 1 y {x}:")) #f-string

if prediccion < numero_aleatorio:
            print("intenta otra vezz. Este numero es muy pequeño.")
elif prediccion >numero_aleatorio:
            print("intenta otra vez. Este numero es muy grande.")

            print(f"¡felicitaciones adivinaste el numero el numero {numero_aleatorio} corectamente!")


adivina_el_numero (10)  