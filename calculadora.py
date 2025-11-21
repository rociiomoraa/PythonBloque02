def sumar(a, b):
    """
    Devuelve la suma de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: Resultado de la suma.
    """
    return a + b


def restar(a, b):
    """
    Devuelve la resta de dos números.

    Parámetros:
        a (float): Minuendo.
        b (float): Sustraendo.

    Retorna:
        float: Resultado de la resta.
    """
    return a - b


def multiplicar(a, b):
    """
    Devuelve la multiplicación de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: Resultado de la multiplicación.
    """
    return a * b


def dividir(a, b):
    """
    Devuelve la división de dos números.

    Parámetros:
        a (float): Dividendo.
        b (float): Divisor.

    Retorna:
        float: Resultado de la división, o None si b es cero.
    """
    if b == 0:
        print("Error: No es posible dividir entre cero.")
        return None
    return a / b


def main():
    # Entrada de datos
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    # Cálculos
    suma = sumar(numero1, numero2)
    resta = restar(numero1, numero2)
    producto = multiplicar(numero1, numero2)
    cociente = dividir(numero1, numero2)

    # Resultados
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {producto}")
    print(f"División: {cociente}")


if __name__ == "__main__":
    main()
