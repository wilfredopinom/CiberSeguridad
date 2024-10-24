import base64

def cifrado_xor(texto, clave):
    # Cifrar/descifrar usando XOR
    resultado = bytearray()
    for i in range(len(texto)):
        # Realizar la operación XOR entre el byte del texto y el byte de la clave (repetida)
        resultado.append(texto[i] ^ clave[i % len(clave)])
    return resultado

def main():
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

            # Convertir el texto y la clave a bytes
            texto_bytes = texto.encode('utf-8')
            clave_bytes = clave.encode('utf-8')

            # Cifrar o descifrar
            resultado = cifrado_xor(texto_bytes, clave_bytes)

            # Convertir el resultado a hexadecimal
            resultado_hex = resultado.hex()
            print("Resultado en hexadecimal:", resultado_hex)

            # Convertir el resultado a Base64
            resultado_base64 = base64.b64encode(resultado).decode('utf-8')
            print("Resultado en Base64:", resultado_base64)
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
