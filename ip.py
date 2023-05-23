import folium  # Работа с широтой и высотой
import requests
from pyfiglet import Figlet  # Библиотека для красивого шрифта


def get_ip(ip='127.0.0.1'):
    """Функция которая выдает нам информацию об IP."""
    try:
        # Делаем гет запрос к адресу и форматируем в JSON формат
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
            }
        # Сортируем наш список key=value
        for h, j in data.items():
            print(f'{h}: {j}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        # Для определения локации используем параметры ширины и высоты
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        # Сохраняем отдельным файлом с разрешением .html

    except requests.exceptions.ConnectionError:
        print('Please, check your connection')


def main():
    """Основная логика приложения."""
    pre_text = Figlet(font='slant')
    print(pre_text.renderText('IP INFO'))
    ip = input('Введите IP адрес: ')

    get_ip(ip=ip)


if __name__ == "__main__":
    main()
