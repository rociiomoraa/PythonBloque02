def registrar_usuario (nombre, edad, ciudad ="Madrid"):

    """
    Muestra en pantalla la información de un usuario utilizando los datos recibidos como parámetros.

    Parámetros:
        nombre (str): El nombre del usuario.
        edad (int): La edad del usuario.
        ciudad (str, opcional): La ciudad del usuario. Por defecto es "Madrid".
    """

    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

def main():

    # Llamada con todos los argumentos posicionales
    registrar_usuario("Ana", 28, "Barcelona")

    # Llamada omitiendo la ciudad para usar el valor por defecto
    registrar_usuario("Luis", 35)

    # Llamada con argumentos nombrados en distinto orden
    registrar_usuario(edad=22, nombre="Marta", ciudad="Valencia")

if __name__ == "__main__":
    main()