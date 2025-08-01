from utils.corefile import read_json, write_json
from utils.validateData import validar_no_vacio, validar_anio

def añadir_elemento(tipo, ruta):
    titulo = input("Título: ").strip()
    if not validar_no_vacio(titulo):
        print("Título inválido.")
        return

    autor_director = input("Autor/Director: ").strip()
    anio = input("Año: ").strip()
    if not validar_anio(anio):
        print("Año inválido.")
        return

    datos = read_json(ruta)
    datos.append({"titulo": titulo, "autor_director": autor_director, "anio": anio})
    write_json(ruta, datos)
    print(f"{tipo} añadido correctamente.")
