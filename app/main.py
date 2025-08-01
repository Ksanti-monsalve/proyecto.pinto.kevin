import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.menu import (
    menu_añadir,
    menu_ver_todos,
    menu_buscar,
    menu_editar,
    menu_eliminar,
    menu_ver_categoria,
    menu_guardar_cargar
)
from utils.screencontrollers import mostrar_titulo

def main():
    while True:
        mostrar_titulo("Colección")

        print("1. Añadir un nuevo elemento")
        print("2. Ver todos los elementos")
        print("3. Buscar un elemento")
        print("4. Editar un elemento")
        print("5. Eliminar un elemento")
        print("6. Ver elementos por categoría")
        print("7. Guardar y Cargar colección")
        print("8. Salir")

        opcion = input("\nSelecciona una opción (1-8): ")

        if opcion == "1":
            menu_añadir()
        elif opcion == "2":
            menu_ver_todos()
        elif opcion == "3":
            menu_buscar()
        elif opcion == "4":
            menu_editar()
        elif opcion == "5":
            menu_eliminar()
        elif opcion == "6":
            menu_ver_categoria()
        elif opcion == "7":
            menu_guardar_cargar()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
