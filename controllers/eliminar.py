from utils.corefile import read_json, write_json

def eliminar_elemento(ruta):
    datos = read_json(ruta)
    for i, e in enumerate(datos, 1):
        print(f"{i}. {e['titulo']} - {e['autor_director']} ({e['anio']})")
    idx = int(input("Número del elemento a eliminar)): ")) - 1
