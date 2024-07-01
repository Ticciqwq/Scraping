import requests
from bs4 import BeautifulSoup

def get_propiedades_buscadorprop(soup):
    propiedades = soup.find_all('div', class_='card-prop__body')
    results = []

    for prop in propiedades:
        direccion_elem = prop.find('div', class_='card-prop__body__arriba__direccion')
        direccion = direccion_elem.get_text(strip=True) if direccion_elem else 'Dirección no especificada'

        price_element = prop.find('div', class_='card-prop__precio')
        if price_element:
            currency_elem = price_element.find('span', class_='card-prop__precio__precios__actual')
            currency = currency_elem.text.strip() if currency_elem else ''
            amount = price_element.get_text(strip=True, separator=' ')
            precio = f'{currency} {amount}'
        else:
            precio = 'Precio no especificado'

        results.append({
            'direccion': direccion,
            'precio': precio
        })
    
    return results
