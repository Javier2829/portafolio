# Portafolio Personal - Flask & Bootstrap 💼

Este es un proyecto de **portafolio personal** desarrollado con **Python (Flask)** y **Bootstrap 5**. La aplicación muestra información personal, habilidades, proyectos y una sección de contacto.

## 🛠️ Tecnologías Utilizadas

- Python
- Flask
- HTML5, CSS3, Bootstrap 5
- Jinja2 (Motor de plantillas)
- (Opcional) Flask-Mail para el formulario de contacto

---

## 🚀 Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/Javier2829/portafolio.git
```

2 **Crear entorno virtual (opcional pero recomendado)**

```bash
python -m venv env
source env/bin/activate  # en Linux/macOS
env\Scripts\activate   # en Windows
```

3 **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4 **Ejecutar la aplicación**

```bash
python app.py
```

> Las dependencias están listadas en `requirements.txt`.

---

## 📂 Estructura del Proyecto

```text
/mi_portafolio/
│
├── /static/
│ └── /img/
│ ├── profile.jpg
│ ├── proyecto1.jpg
│ └── proyecto2.jpg
│
├── /templates/
│ ├── base.html
│ ├── index.html
│ ├── projects.html
│ └── contact.html
│
├── app.py
├── data.py
└── README.md
```

## ✅ Funcionalidades Pendientes

- Integrar un formulario de contacto funcional (con Flask-Mail o servicio externo).

- Añadir un panel de administración para gestionar proyectos.

- Mejorar el diseño responsivo para dispositivos móviles.

---

🤝 Contribuciones
Si deseas mejorar este proyecto, ¡las Pull Requests son bienvenidas! 😄
