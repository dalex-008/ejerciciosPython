jugada_j1 = input("Jugador 1 elige piedra, papel o tijera: ")
jugada_j2 = input("Jugador 2 elige piedra, papel o tijera: ")

if jugada_j1 == jugada_j2:
    print("Empate: ambos eligieron lo mismo")

elif (jugada_j1 == "piedra" and jugada_j2 == "tijera") or \
     (jugada_j1 == "tijera" and jugada_j2 == "papel") or \
     (jugada_j1 == "papel"  and jugada_j2 == "piedra"):
    print("Jugador 1 gana")

else:
    print("Jugador 2 gana")