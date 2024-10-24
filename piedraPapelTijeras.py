import random

print("Bienvenidos al Juego PIEDRA, PAPEL o TIJERAS")
print("INSTRUCCIONES:")
print("1) JUGARÁS CONTRA LA MÁQUINA.")
print("2) DEBES ELEGIR UNA OPCIÓN POR RONDA (PIEDRA, PAPEL, TIJERA).")
print("3) GANARÁ EL PRIMERO QUE GANE 3 PARTIDAS.")
print("¡MUCHA SUERTE!")

nombreJugador = input("Ingresa tu nombre: ")

opciones = ['piedra', 'papel', 'tijeras']

def quienGana(jugador, maquina):
    if jugador == maquina:
        return 'empate'
    elif (jugador == 'piedra' and maquina == 'tijeras') or \
         (jugador == 'papel' and maquina == 'piedra') or \
         (jugador == 'tijeras' and maquina == 'papel'):
        return 'jugador'
    else:
        return 'maquina'

victoriasJugador = 0
victoriasMaquina = 0

while victoriasJugador < 3 and victoriasMaquina < 3:
    jugadorElige = input(f"Es tu turno {nombreJugador}. Elige: piedra, papel o tijeras: ").lower()

    if jugadorElige not in opciones:
        print('Opción no válida, elige de nuevo.')
        continue

    maquina = random.choice(opciones)
    print(f"La máquina elige: {maquina}")

    ganadorRonda = quienGana(jugadorElige, maquina)

    if ganadorRonda == 'jugador':
        print(f'¡Ganaste esta ronda, {nombreJugador}!')
        victoriasJugador += 1
    elif ganadorRonda == 'maquina':
        print('¡La máquina gana esta ronda!')
        victoriasMaquina += 1
    else:
        print('Es un empate.')

    print(f"Marcador -> {nombreJugador}: {victoriasJugador}, Máquina: {victoriasMaquina}")

if victoriasJugador == 3:
    print(f"¡Felicidades {nombreJugador}, ganaste el juego!")
else:
    print("La máquina ganó. ¡Mejor suerte la próxima vez!")
