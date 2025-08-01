from utils.corefile import read_json

def buscar_elemento(ruta):
    termino = input("Buscar por título: ").lower()
    datos = read_json(ruta)
    encontrados = [e for e in datos if termino in e['titulo'].lower()]
    for e in encontrados:
        print(f"{e['titulo']} - {e['autor_director']} ({e['anio']})")
    if not encontrados:
        print("No se encontraron resultados.")
