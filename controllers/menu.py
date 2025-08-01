from utils.screencontrollers import mostrar_titulo
from controllers.anadir import añadir_elemento
from controllers.listar import listar_elementos
from controllers.buscar import buscar_elemento
from controllers.editar import editar_elemento
from controllers.eliminar import eliminar_elemento
from config import LIBROS_PATH, PELICULAS_PATH, MUSICA_PATH

# Submenú 1: Añadir
def menu_añadir():
    while True:
        mostrar_titulo("Añadir un nuevo elemento")
        print("¿Qué tipo de elemento deseas agregar?")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            añadir_elemento("Libro", LIBROS_PATH)
        elif opcion == "2":
            añadir_elemento("Película", PELICULAS_PATH)
        elif opcion == "3":
            añadir_elemento("Música", MUSICA_PATH)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Submenú 2: Ver todos
def menu_ver_todos():
    while True:
        mostrar_titulo("Ver todos los elementos")
        print("¿Qué categoría deseas ver?")
        print("1. Ver todos los libros")
        print("2. Ver todas las películas")
        print("3. Ver toda la música")
        print("4. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            listar_elementos("Libros", LIBROS_PATH)
        elif opcion == "2":
            listar_elementos("Películas", PELICULAS_PATH)
        elif opcion == "3":
            listar_elementos("Música", MUSICA_PATH)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Submenú 3: Buscar
def menu_buscar():
    while True:
        mostrar_titulo("Buscar un elemento")
        print("¿Cómo deseas buscar?")
        print("1. Buscar por título")
        print("2. Buscar por Autor/Director/Artista")
        print("3. Buscar por género")
        print("4. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion in ["1", "2", "3"]:
            print("\nSelecciona la categoría:")
            print("1. Libros\n2. Películas\n3. Música")
            cat = input("Opción: ")
            ruta = None
            if cat == "1": ruta = LIBROS_PATH
            elif cat == "2": ruta = PELICULAS_PATH
            elif cat == "3": ruta = MUSICA_PATH

            if ruta:
                buscar_elemento(ruta)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Submenú 4: Editar
def menu_editar():
    while True:
        mostrar_titulo("Editar un elemento")
        print("¿Qué tipo de cambio deseas realizar?")
        print("1. Editar Título")
        print("2. Editar Autor/Director/Artista")
        print("3. Editar Género")
        print("4. Editar Valoración")
        print("5. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion in ["1", "2", "3", "4"]:
            print("\nSelecciona la categoría:")
            print("1. Libros\n2. Películas\n3. Música")
            cat = input("Opción: ")
            ruta = None
            if cat == "1": ruta = LIBROS_PATH
            elif cat == "2": ruta = PELICULAS_PATH
            elif cat == "3": ruta = MUSICA_PATH

            if ruta:
                editar_elemento(ruta)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

# Submenú 5: Eliminar
def menu_eliminar():
    while True:
        mostrar_titulo("Eliminar un elemento")
        print("¿Cómo deseas eliminar?")
        print("1. Eliminar por título")
        print("2. Eliminar por Identificador único")
        print("3. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion in ["1", "2"]:
            print("\nSelecciona la categoría:")
            print("1. Libros\n2. Películas\n3. Música")
            cat = input("Opción: ")
            ruta = None
            if cat == "1": ruta = LIBROS_PATH
            elif cat == "2": ruta = PELICULAS_PATH
            elif cat == "3": ruta = MUSICA_PATH

            if ruta:
                eliminar_elemento(ruta)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# Submenú 6: Ver por categoría
def menu_ver_categoria():
    while True:
        mostrar_titulo("Ver elementos por categoría")
        print("¿Qué categoría deseas ver?")
        print("1. Ver Libros")
        print("2. Ver Películas")
        print("3. Ver Música")
        print("4. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            listar_elementos("Libros", LIBROS_PATH)
        elif opcion == "2":
            listar_elementos("Películas", PELICULAS_PATH)
        elif opcion == "3":
            listar_elementos("Música", MUSICA_PATH)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Submenú 7: Guardar/Cargar (funcionalidad básica placeholder)
def menu_guardar_cargar():
    while True:
        mostrar_titulo("Guardar y cargar colección")
        print("¿Qué deseas hacer?")
        print("1. Guardar la colección actual")
        print("2. Cargar una colección guardada")
        print("3. Regresar al Menú Principal")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print("Colección guardada.")
        elif opcion == "2":
            print("Colección cargada.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
