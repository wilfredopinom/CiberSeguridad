def cifrado_vigenere(texto, clave):
    resultado = ""
    clave_repetida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]
    
    for i in range(len(texto)):
        letra = texto[i]
        if letra.isalpha():
            # Definir si la letra es mayúscula o minúscula
            inicio = ord('A') if letra.isupper() else ord('a')
            desplazamiento = ord(clave_repetida[i].lower()) - ord('a')
            nueva_letra = chr(inicio + (ord(letra) - inicio + desplazamiento) % 26)
            resultado += nueva_letra
        else:
            # Mantener los caracteres no alfabéticos sin cambios
            resultado += letra

    return resultado

def descifrado_vigenere(texto, clave):
    resultado = ""
    clave_repetida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]
    
    for i in range(len(texto)):
        letra = texto[i]
        if letra.isalpha():
            # Definir si la letra es mayúscula o minúscula
            inicio = ord('A') if letra.isupper() else ord('a')
            desplazamiento = ord(clave_repetida[i].lower()) - ord('a')
            nueva_letra = chr(inicio + (ord(letra) - inicio - desplazamiento) % 26)
            resultado += nueva_letra
        else:
            # Mantener los caracteres no alfabéticos sin cambios
            resultado += letra

    return resultado

if __name__ == "__main__":
    while True:
        # Mostrar el menú de opciones
        print("\nElige una opción:")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        
        opcion = input("Ingresa 1, 2 o 3: ")

        # Salir del programa si elige 3
        if opcion == '3':
            print("Saliendo del programa...")
            break

        # Pedir al usuario que ingrese el texto y la clave si eligió cifrar o descifrar
        if opcion in ['1', '2']:
            texto = input("Ingresa el texto: ")
            clave = input("Ingresa la clave: ")

            if opcion == '1':
                # Opción para cifrar
                cifrado = cifrado_vigenere(texto, clave)
                print("Texto cifrado:", cifrado)
            elif opcion == '2':
                # Opción para descifrar
                descifrado = descifrado_vigenere(texto, clave)
                print("Texto descifrado:", descifrado)
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
