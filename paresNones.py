
import random

# Función para elegir entre pares o nones
def userChoice():
    user_choice = input("Pares o nones?: ").lower()
    # Asegurarse de que el usuario elija 'pares' o 'nones'
    while user_choice != "pares" and user_choice != "nones":
        user_choice = input("Tienes que elegir 'pares' o 'nones': ").lower()
    return user_choice

# Función para elegir un número entre 1 y 5
def userNum():
    user_num = input("Inserta un número en el rango de 1 al 5: ")
    # Validar que sea un número dentro del rango
    while not user_num.isdigit() or int(user_num) < 1 or int(user_num) > 5:
        user_num = input("Tienes que elegir un número en el rango de 1 al 5: ")
    return int(user_num)

# Función para generar un número aleatorio para la máquina
def machineNum():
    return random.randint(1, 5)

# Función principal para el juego de pares y nones
def paresNones():
    user_choice = userChoice()
    user_num = userNum()
    machine_num = machineNum()
    
    # Calcular el resultado sumando los dos números
    result = user_num + machine_num
    
    # Imprimir las elecciones
    print(f"Tu opción: {user_choice}")
    print(f"Tu número: {user_num}")
    print(f"Número de la máquina: {machine_num}")
    
    win_string = "¡Ganaste!"
    lose_string = "Perdiste... Intenta de nuevo."

    # Usar doble return con condiciones separadas
    if user_choice == "pares":
        if result % 2 == 0:
            return win_string
        return lose_string  # Se ejecuta si no es par

    if user_choice == "nones":
        if result % 2 != 0:
            return win_string
        return lose_string  # Se ejecuta si no es impar

# Llamada a la función para jugar
print(paresNones())
