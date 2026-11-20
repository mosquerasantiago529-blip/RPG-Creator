
# ⚔️ RPG Creator

Aplicación web desarrollada con Python y FastAPI que permite crear personajes de RPG de manera aleatoria.

## 🎯 Objetivo

Desarrollar una aplicación web que permita ingresar los datos de un personaje y generar automáticamente sus estadísticas y habilidades.

## 🚀 Tecnologías utilizadas

- Python 3
- FastAPI
- Jinja2
- HTML5
- CSS3
- Pytest
- Uvicorn

## ✨ Funcionalidades

- Crear personajes personalizados.
- Seleccionar raza y clase.
- Generar estadísticas aleatorias.
- Asignar habilidades según la clase.
- Mostrar nivel inicial del personaje.
- Validar los datos del formulario.
- Ejecutar pruebas automatizadas.

## 📁 Estructura del proyecto

```text
RPG_Creator/
│
├── main.py
├── personaje.py
├── test_personaje.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/
```

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar el entorno virtual:

```bash
.\venv\Scripts\Activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

Abrir en el navegador:

http://127.0.0.1:8000

## 🧪 Ejecutar pruebas

```bash
pytest -v
```

El proyecto cuenta con 7 pruebas automatizadas.

## 👨‍💻 Autor

Santiago Mosquera

Ingeniería en Sistemas
