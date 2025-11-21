"""
Este programa gestiona una lista de compras. Solicita al usuario cinco
productos y los añade a una lista. Después muestra la lista completa,
permite eliminar un producto indicado por el usuario y finalmente
muestra la lista ordenada alfabéticamente.
"""


def main():
    compras = []

    # Solicitar 5 productos al usuario
    for _ in range(5):
        producto = input("Introduce un producto: ")
        compras.append(producto)

    # Mostrar lista completa
    print("\nLista de compras completa:")
    print(compras)

    # Eliminar un producto indicado por el usuario
    producto_eliminar = input("\nIntroduce el producto que deseas eliminar: ")

    # Se asume que el usuario introduce un producto existente
    try:
        compras.remove(producto_eliminar)
    except ValueError:
        print("El producto no se encontraba en la lista.")

    # Mostrar lista ordenada
    compras.sort()
    print("\nLista ordenada alfabéticamente:")
    print(compras)


if __name__ == "__main__":
    main()
