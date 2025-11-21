def mostrar_menu ():
    """
    Muestra el menú principal del programa con varias opciones disponibles para el usuario.
    """
    print("=== MENÚ PRINCIPAL ===")
    print("1. Jugar.")
    print("2. Configuración.")
    print("3. Salir.")
    print() # Línea en blanco para mejorar la legibilidad

def main():
    # Primera aparicion del menú
    mostrar_menu()

    # Simulación de que el menú aparece nuevamente
    mostrar_menu()

if __name__ == "__main__":
    main()