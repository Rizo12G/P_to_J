
# Parquet to JSON Convertidor de archivos

Una herramienta simple y eficiente para convertir archivos Parquet a JSON usando Python.
en este repositorio encontraras dos archivos con el mismo codigo un archivo (.py) el cual podras ejecutar desde la terminal directamente y un (.ipynb) es cual esta comentado y explicado como funciona este codigo.
cabe mencionar que necesitaras instalar la libreria (pandas/PyArrow)

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contacto](#contacto)

## Descripción

*Parquet to JSON Converter* es una herramienta diseñada para facilitar la conversión de archivos Parquet a formato JSON.

## Instalación

Sigue estos pasos para instalar el proyecto en tu entorno local:

1. Clona el repositorio:

    bash
    git clone https://github.com/usuario/parquet-to-json.git
    cd parquet-to-json
    

2. Instala las dependencias necesarias usando pip:

    bash
    pip install -r requirements.txt
    

## Uso

Puedes convertir un archivo Parquet a JSON utilizando el siguiente script de Python:

python

import pandas as pd

df = pd.read_parquet('ruta/al/archivo.parquet')

df.to_json('ruta/al/archivo.json', orient='records', lines=True)

## Contacto

Desarrollador: [Gabriel Rizo](https://github.com/Rizo12G)  
Correo: rizo.tnt@gmail.com

