import json
import os

# Estas rutas se definen en config.py
from config import LIBROS_PATH, PELICULAS_PATH, MUSICA_PATH

# Diccionario centralizado para usar en los controladores
RUTAS = {
    "libro": LIBROS_PATH,
    "pelicula": PELICULAS_PATH,
    "musica": MUSICA_PATH
}

# Función para inicializar un archivo JSON vacío si no existe
def inicializar_json(ruta):
    if not os.path.exists(ruta):
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)

# Leer archivo JSON
def read_json(ruta):
    inicializar_json(ruta)
    with open(ruta, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Escribir (sobrescribir) en archivo JSON
def write_json(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Agregar un nuevo elemento al JSON
def append_json(ruta, nuevo_elemento):
    datos = read_json(ruta)
    datos.append(nuevo_elemento)
    write_json(ruta, datos)

# Actualizar un elemento específico
def update_json(ruta, index, nuevo_valor):
    datos = read_json(ruta)
    if 0 <= index < len(datos):
        datos[index] = nuevo_valor
        write_json(ruta, datos)

# Eliminar un elemento por índice
def delete_json(ruta, index):
    datos = read_json(ruta)
    if 0 <= index < len(datos):
        del datos[index]
        write_json(ruta, datos)
