# Variable global
contador = 0


def incrementar():
    """
    Incrementa en 1 la variable global 'contador'.
    Utiliza la palabra clave 'global' para modificarla.
    """
    global contador
    contador += 1


def decrementar():
    """
    Decrementa en 1 la variable global 'contador'.
    Utiliza la palabra clave 'global' para modificarla.
    """
    global contador
    contador -= 1


def mostrar_contador():
    """
    Muestra en pantalla el valor actual de la variable global 'contador'.
    """
    print(f"Contador actual: {contador}")


def main():
    incrementar()
    incrementar()
    decrementar()
    mostrar_contador()


if __name__ == "__main__":
    main()
