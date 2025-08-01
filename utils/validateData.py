def validar_no_vacio(texto):
    return texto.strip() != ""

def validar_anio(texto):
    return texto.isdigit() and 1000 <= int(texto) <= 2100
