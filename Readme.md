# TRABAJO PRACTICO-PROGRAMACION AVANZADA WEB SCRAPING con BeautifulSoup.
Repositorio para el trabajo práctico de programación avanzada, Web Scraping con Beautiful Soup 4.


## Descripción

Esta aplicación es una herramienta simple que permite obtener direcciones y precios de propiedades en venta o en alquiler en dos sitios web: [Argenprop](https://www.argenprop.com/) y [BuscadorProp](https://www.buscadorprop.com.ar/). Utiliza las bibliotecas `requests` y `BeautifulSoup` para hacer scraping de los datos.

## Estructura del Proyecto

El código está dividido en los siguientes archivos:

1. **Readme.md**: Este archivo, que proporciona una descripción del funcionamiento de la aplicación.

## Instalación y Uso

1. Asegúrese de tener Python 3.x instalado en su sistema.
2. Instale las dependencias necesarias:
    ```sh
    pip install requests beautifulsoup4
    ```
3. Ejecute el archivo `main.py` para iniciar la aplicación:
    ```sh
    python main.py buscadorprop casa venta lanus
    ```
4. seleccione el sitio web desde el cual desea obtener las propiedades.

## Notas

- La estructura HTML de los sitios web puede cambiar con el tiempo, lo cual podría afectar la capacidad de la aplicación para hacer scraping correctamente. Es posible que se requieran ajustes en el método `parse_properties` para adaptarse a estos cambios.
- La aplicación está diseñada para ser un ejemplo simple y puede mejorarse con características adicionales como manejo de errores más robusto, paginación y opciones de búsqueda más avanzadas.
