Index
- [Installation](#Installation)
- [Folder&nbsp;structure](#Folder&nbsp;structure)

## Installation
- <strong><em>conda create --name django_env python=3.8</em></strong>
- conda activate django_env 
- pip install -r requirements.txt
- python db_generation.py

&nbsp;

## Folder structure

- El Directorio <strong><em>src</em></strong> cuenta con 5 sub directorios:
  1. Panel_null_vendors. Constituye el proyecto django iniciado con django-admin startproject
  2. Datatable_null_vendors. Constituye la Django app que incluye los modelos necesarios
  para la generación del panel.
  3. Pages. Incluye las vistas necesarias para la generación del panel.
  4. Static. Incluye ficheros JS necesarios para el diseño front del panel.
  5. Templates. Incluyen los ficheros HTML que se muestran en el front del panel.

El proyecto Django utiliza la DB postgres generada en el repositorio de la Parte1 de la prueba.
