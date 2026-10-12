# 📚 Seminario de Integración

**Autor:** Rahí Ruilova

## 📖 Descripción de la materia

Este repositorio contiene los ejercicios, prácticas y proyectos desarrollados en la materia **Seminario de Integración**.

El objetivo es reforzar los conocimientos de programación y desarrollo web mediante el repaso de tecnologías como **Python, uv, FastAPI, TypeScript y Angular**, integrando los conceptos aprendidos en la construcción de aplicaciones modernas.

Durante la materia se trabajará con ejercicios prácticos, desarrollo de APIs, aplicaciones web y proyectos que permitan aplicar buenas prácticas de programación, organización del código y gestión de dependencias.

---

## 🎯 Objetivos

- Reforzar los fundamentos de programación con Python.
- Aprender a gestionar proyectos y dependencias utilizando uv.
- Desarrollar APIs REST con FastAPI.
- Comprender los fundamentos de TypeScript.
- Construir interfaces web con Angular.
- Integrar el frontend con el backend mediante APIs.
- Aplicar buenas prácticas de desarrollo y organización de proyectos.
- Utilizar Git y GitHub para el control de versiones.

---

## 🛠️ Tecnologías utilizadas

### 🐍 Python

**Python** es un lenguaje de programación de alto nivel, conocido por su sintaxis sencilla y legible. Se utiliza para desarrollar aplicaciones, automatizar tareas, procesar datos y construir servicios backend.

**Conceptos que se repasarán:**
- Variables y tipos de datos.
- Operadores y estructuras de control.
- Funciones y módulos.
- Listas, tuplas, conjuntos y diccionarios.
- Programación orientada a objetos.
- Manejo de excepciones.
- Entornos virtuales y gestión de paquetes.

**Ejemplo:**

def saludar(nombre: str) -> str: return f"Hola, {nombre}!"

print(saludar("Mundo"))


### ⚡ uv

**uv** es una herramienta rápida para gestionar proyectos Python, dependencias, versiones del intérprete y entornos virtuales.

Permite simplificar la configuración de proyectos y mantener las dependencias organizadas y reproducibles.

**Conceptos que se estudiarán:**
- Creación de proyectos Python.
- Gestión de dependencias.
- Creación y administración de entornos virtuales.
- Uso de `pyproject.toml`.
- Gestión del archivo `uv.lock`.
- Ejecución de scripts y aplicaciones.

**Comandos básicos:**

Crear un proyecto

uv init
Crear y sincronizar el entorno del proyecto

uv sync
Agregar una dependencia

uv add fastapi
Agregar Uvicorn para ejecutar la aplicación

uv add "uvicorn[standard]"
Ejecutar un archivo Python

uv run main.py
Ejecutar una aplicación con Uvicorn

uv run uvicorn main:app --reload


**Nota:** uv administra normalmente los entornos virtuales de los proyectos mediante una carpeta `.venv`.

### 🚀 FastAPI

**FastAPI** es un framework moderno de Python para desarrollar APIs web. Permite crear servicios backend utilizando las anotaciones de tipos de Python y facilita la validación de datos mediante Pydantic.

Además, genera documentación interactiva de los endpoints de forma automática.

**Conceptos que se estudiarán:**
- Creación de APIs REST.
- Métodos HTTP: GET, POST, PUT, PATCH y DELETE.
- Rutas y parámetros.
- Validación de datos.
- Modelos con Pydantic.
- Códigos de estado HTTP.
- Manejo de errores.
- Documentación automática con Swagger UI.
- Integración con bases de datos.
- Comunicación entre frontend y backend.

**Ejemplo:**

from fastapi import FastAPI

app = FastAPI( title="API de Seminario de Integración" )

@app.get("/") def inicio(): return {"mensaje": "Bienvenido a FastAPI"}

@app.get("/saludo/{nombre}") def saludar(nombre: str): return {"mensaje": f"Hola, {nombre}"}


Para ejecutar la aplicación:

uv run uvicorn main:app --reload


Una vez iniciada, la API estará disponible normalmente en:

- **API:** http://127.0.0.1:8000
- **Documentación Swagger:** http://127.0.0.1:8000/docs
- **Documentación alternativa:** http://127.0.0.1:8000/redoc

### 🔷 TypeScript

**TypeScript** es un lenguaje de programación basado en JavaScript que incorpora un sistema de tipos estático. Permite detectar numerosos errores durante el desarrollo y facilita la organización de aplicaciones grandes.

Es una tecnología fundamental para el desarrollo de aplicaciones con Angular.

**Conceptos que se estudiarán:**
- Tipos de datos.
- Variables y constantes.
- Funciones tipadas.
- Interfaces y tipos personalizados.
- Clases y objetos.
- Programación orientada a objetos.
- Genéricos.
- Módulos e importaciones.
- Tipado de parámetros y valores de retorno.
- Uso de TypeScript en aplicaciones web.

**Ejemplo:**

interface Estudiante { nombre: string; edad: number; activo: boolean; }

function presentar(estudiante: Estudiante): string { return Soy ${estudiante.nombre} y tengo ${estudiante.edad} años.; }

const estudiante: Estudiante = { nombre: "Carlos", edad: 22, activo: true };

console.log(presentar(estudiante));


### 🅰️ Angular

**Angular** es un framework de desarrollo web mantenido por Google que permite construir aplicaciones frontend mediante componentes, servicios y una arquitectura organizada.

Utiliza TypeScript como lenguaje principal y proporciona herramientas para crear aplicaciones web dinámicas y escalables.

**Conceptos que se estudiarán:**
- Estructura de un proyecto Angular.
- Componentes y plantillas.
- Directivas y vinculación de datos.
- Interpolación y property binding.
- Event binding.
- Formularios.
- Servicios e inyección de dependencias.
- Enrutamiento entre páginas.
- Comunicación entre componentes.
- Consumo de APIs REST mediante HttpClient.
- Manejo de peticiones HTTP.
- Organización de aplicaciones por funcionalidades.

**Ejemplo de componente:**

import { Component } from '@angular/core';

@Component({ selector: 'app-inicio', standalone: true, template: <h1>{{ titulo }}</h1> <p>Bienvenido a Seminario de Integración.</p> }) export class InicioComponent { titulo = 'Mi primera aplicación Angular'; }


Este componente muestra cómo definir una propiedad en TypeScript y utilizarla dentro de una plantilla HTML.

---

## 🔗 Integración de tecnologías

Uno de los objetivos principales de la materia será comprender cómo se comunican las diferentes tecnologías para construir una aplicación completa.

La arquitectura general será:

┌──────────────────────────────────────┐ │ FRONTEND │ │ │ │ Angular │ │ TypeScript │ │ │ │ └─────────────────┼────────────────────┘ │ │ Peticiones HTTP │ Formato JSON ▼ ┌──────────────────────────────────────┐ │ BACKEND │ │ │ │ FastAPI │ │ Python │ │ │ │ └─────────────────┼────────────────────┘ │ ▼ ┌──────────────────────────────────────┐ │ BASE DE DATOS │ │ │ │ Persistencia de información │ └──────────────────────────────────────┘


**Flujo de funcionamiento:**

1. El usuario interactúa con la interfaz desarrollada en Angular.
2. Angular realiza una petición HTTP al backend.
3. FastAPI recibe la petición y valida los datos.
4. Python ejecuta la lógica de negocio.
5. El backend consulta o modifica la información almacenada, cuando corresponde.
6. FastAPI devuelve una respuesta, generalmente en formato JSON.
7. Angular procesa la respuesta y actualiza la interfaz.

---

## 📂 Estructura del repositorio

El repositorio estará organizado por tecnologías, ejercicios y proyectos para facilitar el aprendizaje y el seguimiento de las actividades.

seminario-integracion/ │ ├── README.md ├── .gitignore │ ├── python/ │ ├── fundamentos/ │ ├── funciones/ │ ├── poo/ │ └── ejercicios/ │ ├── uv/ │ ├── creacion-proyectos/ │ ├── dependencias/ │ └── entornos-virtuales/ │ ├── fastapi/ │ ├── fundamentos/ │ ├── rutas/ │ ├── validaciones/ │ └── api-rest/ │ ├── typescript/ │ ├── fundamentos/ │ ├── funciones/ │ ├── interfaces/ │ └── poo/ │ ├── angular/ │ ├── componentes/ │ ├── servicios/ │ ├── formularios/ │ └── consumo-api/ │ └── proyectos-integradores/ ├── backend/ └── frontend/


*La estructura es una propuesta inicial y podrá modificarse conforme avance la materia.*

---

## 💻 Requisitos previos

Para trabajar con los proyectos del repositorio se recomienda instalar las siguientes herramientas:

Herramienta	Descripción
Python	Lenguaje utilizado para el backend.
uv	Gestión de proyectos, dependencias y entornos Python.
Node.js	Entorno de ejecución necesario para las herramientas de Angular.
npm	Administrador de paquetes de Node.js.
Angular CLI	Herramienta para crear y administrar proyectos Angular.
Git	Sistema de control de versiones.
Visual Studio Code	Editor de código recomendado.
📋 Instalación y configuración
1. Verificar Python y uv

python --version
uv --version

2. Verificar Node.js y npm

node --version
npm --version

3. Instalar Angular CLI

npm install -g @angular/cli

Verificar la instalación:

ng version

4. Crear un proyecto Python

mkdir mi-proyecto
cd mi-proyecto

uv init
uv add fastapi "uvicorn[standard]"

Crear un archivo main.py con una aplicación FastAPI y ejecutarla:

uv run uvicorn main:app --reload

5. Crear un proyecto Angular

Desde el directorio donde se almacenarán los proyectos frontend:

ng new mi-aplicacion
cd mi-aplicacion
ng serve

La aplicación estará disponible normalmente en:

http://localhost:4200
📅 Actividades académicas

Durante la materia se podrán desarrollar las siguientes actividades:

    Repaso de Python: ejercicios de lógica, funciones y programación orientada a objetos.
    Gestión de proyectos con uv: creación de entornos virtuales y administración de dependencias.
    Desarrollo backend: construcción de APIs REST utilizando FastAPI.
    Fundamentos de TypeScript: tipos, interfaces, funciones y clases.
    Desarrollo frontend: creación de componentes y páginas con Angular.
    Integración de aplicaciones: conexión entre Angular y FastAPI.
    Proyectos prácticos: desarrollo de aplicaciones que integren las tecnologías estudiadas.

🌱 Buenas prácticas

Durante el desarrollo de los ejercicios y proyectos se procurará:

    Utilizar nombres descriptivos para variables, funciones, clases y archivos.
    Organizar el código en módulos y componentes reutilizables.
    Mantener las dependencias declaradas en los archivos de configuración.
    Utilizar entornos virtuales para aislar los proyectos Python.
    No subir carpetas .venv/ ni node_modules/ al repositorio.
    No publicar contraseñas, tokens ni claves privadas.
    Utilizar Git para registrar los cambios.
    Escribir documentación para explicar los proyectos.
    Validar los datos recibidos por las APIs.
    Mantener una separación clara entre frontend y backend.

📚 Recursos oficiales

    Python: https://docs.python.org/3/
    uv: https://docs.astral.sh/uv/
    FastAPI: https://fastapi.tiangolo.com/
    TypeScript: https://www.typescriptlang.org/docs/
    Angular: https://angular.dev/
    Node.js: https://nodejs.org/docs/
    Git: https://git-scm.com/doc/

👨‍💻 Autoría y contexto académico

Materia: Seminario de Integración

Propósito: Repaso, práctica e integración de tecnologías para el desarrollo de aplicaciones web.

Tecnologías principales: Python, uv, FastAPI, TypeScript y Angular.

Este repositorio tiene fines académicos y servirá como espacio de organización, documentación y seguimiento de los ejercicios y proyectos desarrollados durante la materia.

Seminario de Integración — Aprender, practicar e integrar tecnologías para construir soluciones de software.