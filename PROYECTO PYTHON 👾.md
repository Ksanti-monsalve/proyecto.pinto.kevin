# PROYECTO PYTHON 👾

# 📚 SISTEMA DE GESTIÓN DE COLECCIÓN MULTIMEDIA EN CONSOLA (PYTHON)

Este proyecto es una aplicación de consola desarrollada en Python que permite **gestionar una colección de libros, películas y música** de forma organizada, funcional y persistente. Está pensada como una herramienta educativa para aplicar conceptos fundamentales de programación modular, manejo de archivos JSON, validación de datos, y diseño estructurado de proyectos en Python.

---

## 🧠 Objetivo del proyecto

El propósito de este sistema es facilitar el registro y la gestión de distintos tipos de contenido multimedia desde una interfaz de texto interactiva. El usuario puede:

- Añadir elementos a su colección personal.
- Guardarlos automáticamente en archivos separados.
- Mantener organizados los datos por categoría (libros, películas, música).
- Trabajar con una arquitectura clara y escalable.

Este sistema es ideal como base para futuros desarrollos más avanzados (por ejemplo: exportar, buscar, editar o migrar a una interfaz gráfica).

---

## 📁 Estructura del proyecto

El código está organizado de forma modular, distribuyendo la lógica en carpetas separadas por responsabilidad:

## estructura del proyecto 

│
├── app/
│   └── main.py
│
├── controlles/
│   ├── añadir.py
│   ├── buscar.py
│   ├── editar.py
│   ├── eliminar.py
│   ├── listar.py
│   └── menus.py
│
├── data/
│   ├── libros.json
│   ├── musica.json
│   └── peliculas.json
│
├── utils/
│   ├── corefile.py
│   ├── screencontrollers.py
│   └── validateData.py
│
└── config.py

---

## 🧾 Descripción de los componentes principales

### 🔧 `config.py`

Archivo clave que centraliza las rutas de almacenamiento de los archivos `.json`. Evita repetir rutas manualmente en cada módulo, mejorando la mantenibilidad del proyecto.

```python
LIBROS_PATH = "data/libros.json"
PELICULAS_PATH = "data/peliculas.json"
MUSICA_PATH = "data/musica.json"
```

