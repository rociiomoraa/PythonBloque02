"""
Este programa define una tupla con información personal (nombre, edad
y ciudad), desempaqueta sus valores en variables independientes y
muestra la información en pantalla. Se utiliza una tupla porque los
datos no deben modificarse.
"""

def main():
    # Tupla con la información de la persona
    persona = ("Ana", 25, "Madrid")

    # Desempaquetado de tupla
    nombre, edad, ciudad = persona

    # Mostrar la información
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")


if __name__ == "__main__":
    main()
