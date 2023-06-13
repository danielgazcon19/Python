def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Verifica si el carácter es una letra
            codigo = ord(caracter) + desplazamiento
            if caracter.isupper():
                limite = ord('Z')
            else:
                limite = ord('z')
            if codigo > limite:  # Vuelve al principio del alfabeto si se excede el límite
                codigo -= 26
            resultado += chr(codigo)
        else:
            resultado += caracter
    return resultado


def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

texto_original = input("Escriba el texto a cifrar: ")
desplazamiento = int(input("Ingrese el valor de desplazamiento: "))

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)

print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)
