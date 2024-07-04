import requests
from bs4 import BeautifulSoup
import argparse
from ScrapingBuscadorprop import get_propiedades_buscadorprop

class Propiedad:
    def __init__(self, direccion, precio):
        self.direccion = direccion
        self.precio = precio

    def __str__(self):
        return f'Dirección: {self.direccion}\nPrecio: {self.precio}\n-------------------'


class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_properties(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Error al realizar la solicitud HTTP: {e}')
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        return self.parse_properties(soup)


class ArgenpropScraper(Scraper):
    def parse_properties(self, soup):
        propiedades = soup.find_all('div', class_='card__details-box')
        results = []

        for prop in propiedades:
            direccion_elem = prop.find('p', class_='card__address')
            direccion = direccion_elem.get_text(strip=True) if direccion_elem else 'Dirección no especificada'

            price_element = prop.find('p', class_='card__price')
            if price_element:
                currency_elem = price_element.find('span', class_='card__currency')
                currency = currency_elem.text.strip() if currency_elem else ''
                amount = price_element.get_text(strip=True, separator=' ')
                precio = f'{currency} {amount}'
            else:
                precio = 'Precio no especificado'

            results.append(Propiedad(direccion, precio))

        return results

    def build_url(self, tipo_propiedad, operacion, localidad):
        tipo_map = {'departamento': 'departamentos', 'casa': 'casas'}
        operacion_map = {'venta': 'venta', 'alquiler': 'alquiler'}
        return f'https://www.argenprop.com/{tipo_map[tipo_propiedad]}/{operacion_map[operacion]}/{localidad}'


class BuscadorpropScraper(Scraper):
    def parse_properties(self, soup):
        propiedades = get_propiedades_buscadorprop(soup)
        results = []

        for prop in propiedades:
            direccion = prop.get('direccion', 'Dirección no especificada')
            precio = prop.get('precio', 'Precio no especificado')
            results.append(Propiedad(direccion, precio))

        return results

    def build_url(self, tipo_propiedad, operacion, localidad):
        tipo_map = {'departamento': 'departamentos-loft-semipiso', 'casa': 'casas-dormitorios'}
        operacion_map = {'venta': 'venta', 'alquiler': 'alquiler'}
        return f'https://www.buscadorprop.com.ar/{tipo_map[tipo_propiedad]}-{operacion_map[operacion]}-{localidad}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Buscar propiedades en Argenprop o Buscadorprop')
    parser.add_argument('base_url', choices=['argenprop', 'buscadorprop'], help='El sitio web a utilizar: argenprop o buscadorprop')
    parser.add_argument('tipo_propiedad', choices=['departamento', 'casa'], help='El tipo de propiedad: departamento o casa')
    parser.add_argument('operacion', choices=['venta', 'alquiler'], help='El tipo de operación: venta o alquiler')
    parser.add_argument('localidad', help='La localidad para buscar propiedades')

    args = parser.parse_args()

    if args.base_url == 'argenprop':
        scraper = ArgenpropScraper(args.base_url)
    else:
        scraper = BuscadorpropScraper(args.base_url)

    url = scraper.build_url(args.tipo_propiedad, args.operacion, args.localidad)

    print(f'Buscando propiedades en: {url}')
    propiedades = scraper.get_properties(url)
    for prop in propiedades:
        print(prop)
