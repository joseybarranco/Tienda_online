# Manual Técnico del Proyecto
## IES Abdera de Adra (Almería)
### CFGS Desarrollo de Aplicaciones Web (DAW)
#### Curso 2024-2025

---

## 1. Información General
- **Nombre del Proyecto:** Tienda Online  
- **Autores:** José Ignacio Barranco Ruiz  
- **Fecha de creación:**8 de Abril de 2025  
- **Última actualización:** 8 de Abril de 2025
- **Profesor Responsable:** José Ramon  

---

## 2. Descripción del Proyecto
Este proyecto trata de crear una aplicación para gestionar una tienda online que gestiona usuarios tanto clientes como administradores, gestionar productos físicos y digitales. Los clientes pueden crear reseñas de los productos que han comprado y pueden hacer pedidos de los productos de la tienda. También es capaz de gestionar pedidos que permiten vender productos de la tienda.

---

## 3. Tecnologías Utilizadas
Listado de tecnologías empleadas en el desarrollo: 
- **Backend:**  Python   
- **Control de Versiones:** GitKraken y GitHub  


---

## 4. Requisitos Previos
Lista de software necesario para ejecutar el proyecto:
- Python y dependencias necesarias  
- Github  

---

## 5. Estructura del Proyecto
```plaintext
.
├── docs
│   ├── build
│   │   ├── doctrees
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   ├── modules.doctree
│   │   │   └── proyecto.doctree
│   │   └── html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── _modules
│   │       │   ├── index.html
│   │       │   └── proyecto
│   │       │       ├── cliente.html
│   │       │       └── producto.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── proyecto.html
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       ├── _sources
│   │       │   ├── index.rst.txt
│   │       │   ├── modules.rst.txt
│   │       │   └── proyecto.rst.txt
│   │       └── _static
│   │           ├── alabaster.css
│   │           ├── base-stemmer.js
│   │           ├── basic.css
│   │           ├── custom.css
│   │           ├── doctools.js
│   │           ├── documentation_options.js
│   │           ├── file.png
│   │           ├── forkme_right_darkblue_121621.png
│   │           ├── language_data.js
│   │           ├── minus.png
│   │           ├── plus.png
│   │           ├── pygments.css
│   │           ├── searchtools.js
│   │           ├── spanish-stemmer.js
│   │           ├── sphinx_highlight.js
│   │           └── translations.js
│   ├── make.bat
│   ├── Makefile
│   └── source
│       ├── conf.py
│       ├── index.rst
│       ├── modules.rst
│       ├── proyecto.rst
│       ├── _static
│       └── _templates
├── proyecto
│   ├── cliente.py
│   ├── __init__.py
│   ├── main.py
│   ├── pedido.py
│   ├── productoDigital.py
│   ├── producto.py
│   ├── __pycache__
│   │   ├── cliente.cpython-312.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── pedido.cpython-312.pyc
│   │   ├── producto.cpython-312.pyc
│   │   ├── productoDigital.cpython-312.pyc
│   │   └── reseña.cpython-312.pyc
│   └── reseña.py
└── README

 
```

---


## 6. Seguridad
- Validaciones de entrada de datos  
- Implementación de roles de usuario  

---

## 7. Conclusión
- Evaluación del desarrollo: Se han implementado la programación orientada a objetos y la relación entre todos los elementos de la aplicación.  
- Falta implementar la base de datos y las conexiones de ésta, asi como un front de la aplicación.  

---


