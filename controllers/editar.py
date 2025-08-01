from utils.corefile import read_json, write_json

def editar_elemento(ruta):
    datos = read_json(ruta)
    for i, e in enumerate(datos, 1):
        print(f"{i}. {e['titulo']} - {e['autor_director']} ({e['anio']})")
    idx = int(input("Número del elemento a editar: ")) - 1
    if 0 <= idx < len(datos):
        datos[idx]['titulo'] = input("Nuevo título: ")
        datos[idx]['autor_director'] = input("Nuevo autor/director: ")
        datos[idx]['anio'] = input("Nuevo año: ")
        write_json(ruta, datos)
        print("Elemento editado.")
    else:
        print("Índice inválido.")
