READ ME BUENOOOOOOOOOO


# GymAPP

Este es un proyecto desarrollado con Django:
- Una plataforma donde los usuarios pueden publicar y ver sus ejercicios y los de otros usuarios.
- Un asistente de IA que recomienda ejercicios personalizados según las necesidades del usuario.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
  ```bash
  sudo apt install python-is-python3
  ```
- Git  
  ```bash
  sudo apt install git -y
  ```
- pip (viene con Python)  
  ```bash
  sudo apt update
  sudo apt install python3-pip
  ```
- virtualenv  
  ```bash
  pip3 install virtualenv
  ```
- MySQL 5.8 o superior  
  ```bash
  sudo apt install mysql-server -y
  ```
- Comunicar Django con MySQL  
  ```bash
  pip install django
  sudo apt install libmysqlclient-dev python3-dev
  ```

---

## Instalación en entorno local

Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local.

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/rriitaa/tfg-final-rita.git
cd tu-repo
```

### 2. Crear y activar un entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows (si procede)
venv\Scripts\activate

# Activar en macOS / Linux (si procede)
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no tienes el archivo requirements.txt, puedes generarlo con:

```bash
pip freeze > requirements.txt
```

Asegúrate de que el archivo incluya al menos:

```
Django==4.2
openai==1.78.0
```

### 4. Configurar variables de entorno

Abre el archivo views.py y añade tu clave de OpenAI

```
OPENAI_API_KEY=tu_clave_de_openai_aqui
```

#### Cómo obtener la clave de OpenAI:

1. Ve a https://platform.openai.com
2. Crea una cuenta o inicia sesión.
3. Accede a tu perfil (esquina superior derecha) → View API Keys
4. Haz clic en "Create new secret key"
5. Copia la clave generada y pégala en el archivo `.env` como se indicó arriba.

Y asegúrate de que en tu `settings.py` esté configurado para leer la API Key.  
Abre el archivo `settings.py` ubicado en: `GymAI/GymAI/settings.py` y añade lo siguiente:

```python
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

Asegúrate de añadir el archivo `.env` al `.gitignore`. Dentro del `.gitignore` debe aparecer así:

```
venv/
__pycache__/
*.pyc
*.pyo
.DS_Store
staticfiles/
static/
manage.py
.vscode
.env
```

### 5. Aplicar migraciones de base de datos

```bash
python manage.py migrate
```

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor

Abre tu navegador en:  
http://127.0.0.1:8000/

---

### En resumen:

```bash
.\venv\Scripts\activate
cd .\GymAI\
python manage.py runserver
```

---

## ESTRUCTURA DEL PROYECTO (se debería ver algo así):

```
GymAI/
├── manage.py
├── README.md
├── .gitignore
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── signals.py
├── templates/
│   └── core/
│       ├── categorias.html
│       ├── comienza-entreno.html
│       ├── comunidad.html
│       ├── ejercicios_cardio.html
│       ├── ejercicios_espalda.html
│       ├── ejercicios_flexibilidad.html
│       ├── ejercicios_fuerza.html
│       ├── ejercicios_gluteos.html
│       ├── ejercicio-single.html
│       ├── ia-asistente.html
│       ├── index.html
│       ├── inicio.html
│       ├── login.html
│       ├── mis-publis.html
│       ├── perfil.html
│       ├── recuperar.html
│       ├── signup.html
│       ├── sub-ejers.html
├── tfg/
│   ├── settings.py
│   ├── urls.py
```

