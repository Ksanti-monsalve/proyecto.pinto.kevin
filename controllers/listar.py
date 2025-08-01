from utils.corefile import read_json
from utils.screencontrollers import mostrar_titulo

def listar_elementos(tipo, ruta):
    mostrar_titulo(f"{tipo.upper()} REGISTRADOS")
    datos = read_json(ruta)
    if not datos:
        print("No hay elementos registrados.")
    for i, item in enumerate(datos, 1):
        print(f"{i}. {item['titulo']} - {item['autor_director']} ({item['anio']})")
