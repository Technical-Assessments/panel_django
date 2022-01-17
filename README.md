## Index
- [Description](#Description)
- [Installation](#Installation)
- [Currently under develop](#Currently-under-develop)
- [Folder structure](#Folder-structure)

## Description

Este pequeño proyecto es la implementación de la technical assessment descrita en el pdf adjunto en la raiz del repositorio. Consiste en la extracción, manipulación, almacenamiento y visualización de una serie de datos de viajes de taxis en la ciudad de New York para un determinado periodo de tiempo (2020 January). Tanto el año como el/los meses se pueden modificar en el archivo <em>db_generation.py</em>. En tal caso, habría que relanzar ese mismo script (4º paso de la sección Instalación).

## Installation
- <em>conda create --name django_env python=3.8</em>
- <em>conda activate django_env</em>
- <em>pip install -r requirements.txt</em>
- <em>python src/manage.py makemigrations</em>
- <em>python src/manage.py migrate</em>
- <em>python src/manage.py runserver</em>
- <em>python db_generation.py</em> (Este paso puede tardar en torno a 1-3 minutos ya que está parseando e insertando en BD más 6 millones de filas de datos, para el escenario por defecto January 2020)


&nbsp;

## Currently under develop
- Actualmente tanto el Panel como la API tardan demasiado en cargar, dado que el máximo de Pagination no está siendo tenido en cuenta.
- Funcionalidad Edit record + Aplicar cambios

## Folder structure<a name="Folder-structure"></a>

- El Directorio <strong><em>src</em></strong> cuenta con 6 sub directorios:
  1. Panel_null_vendors. Constituye el proyecto django iniciado con django-admin startproject
  2. Datatable_null_vendors. Constituye la Django app que incluye los modelos necesarios
  para la generación del panel.
  3. Pages. Incluye las vistas necesarias para la generación del panel.
  4. Static. Incluye ficheros JS necesarios para el diseño front del panel.
  5. Templates. Incluyen los ficheros HTML que se muestran en el front del panel.
  6. Database. Contiene la basse de datos generada con el script db_generation.py

- El directorio <strong><em>data_scripts</em></strong>
- El directorio <strong><em>Assessment_answers</em></strong>
