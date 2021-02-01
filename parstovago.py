import requests
from bs4 import BeautifulSoup
import csv


try:
    import configparser
except ImportError:
    import ConfigParser as configparser
    from collections import OrderedDict



config = configparser.ConfigParser()
config.read('config.ini')

URL=str(config.get("Settings","urll"))
koltovara=str(config.get("Settings","koltovara"))
katal=str(config.get("Settings","katal"))






HOST='https://tavago.ru'

HEADERS ={
           'ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
          }
CSV=katal+'.csv'

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')


    cards =[]
    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='title').find('h2').find('a').get_text(strip=True),
               'link_product': HOST + item.find('div', class_='title').find('a').get('href'),
                'wrap-param': item.find('div', class_='features').get_text(strip=True),
                'img-product': HOST + item.find('div', class_='uk-inline-clip').find('img', class_='img-product').get('src'),
                'price': item.find('div', class_='price').get_text(strip=True)

            }
        )
    return cards
def s_file(items, path):
    with open(path,'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([ 'Название', 'ССылка на прордукт','картинка','Цена', 'Характеристики' ])

        for item in items:
            #словарь исключенных слов
            item['wrap-param'] = item['wrap-param'].replace("Тип ручки", ";Тип ручки;")
            item['wrap-param'] = item['wrap-param'].replace("Тип проходного сечения", ";Тип проходного сечения;")
            item['wrap-param'] = item['wrap-param'].replace("Подробнее о товаре", "")
            item['wrap-param'] = item['wrap-param'].replace("Рабочая температура", ";Рабочая температура;")
            item['wrap-param'] = item['wrap-param'].replace("Диаметр присоединения", ";Диаметр присоединения;")
            item['wrap-param'] = item['wrap-param'].replace("Материал изготовления", ";Материал изготовления;")


            item['wrap-param'] = item['wrap-param'].replace("Условная пропускная способность термостатического клапана", ";Условная пропускная способность термостатического клапана;")
            item['wrap-param'] = item['wrap-param'].replace("Пропускная способность", ";Пропускная способность;")
            item['wrap-param'] = item['wrap-param'].replace("\"", "")
            item['wrap-param'] = item['wrap-param'].replace("Тип резьбового фитинга", ";Тип резьбового фитинга;")
            item['wrap-param'] = item['wrap-param'].replace("Резьба", ";Резьба;")
            item['wrap-param'] = item['wrap-param'].replace("Диаметр", ";Диаметр;")

            item['wrap-param'] = item['wrap-param'].replace("КПД",";КПД;")
            item['wrap-param'] = item['wrap-param'].replace("Тепловая мощность", ";Тепловая мощность;")
            item['wrap-param'] = item['wrap-param'].replace("Вид топлива", ";Вид топлива;")
            item['wrap-param'] = item['wrap-param'].replace("Количество контуров", ";Количество контуров;")
            item['wrap-param'] = item['wrap-param'].replace("Тип установки", ";Тип установки;")

            item['wrap-param'] = item['wrap-param'].replace("Точность регулирования температуры теплоносителя", ";Точность регулирования температуры теплоносителя;")
            item['wrap-param'] = item['wrap-param'].replace("Количество насадок", ";Количество насадок;")
            item['wrap-param'] = item['wrap-param'].replace("Количество газовых сопел", ";Количество газовых сопел;")
            item['wrap-param'] = item['wrap-param'].replace("Наружный диаметр насадки", ";Наружный диаметр насадки;")
            item['wrap-param'] = item['wrap-param'].replace("Диапазон мощности", ";Диапазон мощности;")
            item['wrap-param'] = item['wrap-param'].replace("Расход сжиженного газа", ";Расход сжиженного газа;")
            item['wrap-param'] = item['wrap-param'].replace("Тип камеры сгорания", ";Тип камеры сгорания;")
            item['wrap-param'] = item['wrap-param'].replace("Тип дымохода", ";Тип дымохода;")

            item['wrap-param'] = item['wrap-param'].replace("Элемент дымохода", ";Элемент дымохода;")
            item['wrap-param'] = item['wrap-param'].replace("Напряжение", ";Напряжение;")
            item['wrap-param'] = item['wrap-param'].replace("Наружный диаметр насадки", ";Наружный диаметр насадки;")
            item['wrap-param'] = item['wrap-param'].replace("Диапазон мощности", ";Диапазон мощности;")
            item['wrap-param'] = item['wrap-param'].replace("Расход сжиженного газа", ";Расход сжиженного газа;")
            item['wrap-param'] = item['wrap-param'].replace("Тип камеры сгорания", ";Тип камеры сгорания;")


            item['wrap-param'] = item['wrap-param'].replace("Уровень шума", ";Уровень шума;")
            item['wrap-param'] = item['wrap-param'].replace("Длина", ";Длина;")
            item['wrap-param'] = item['wrap-param'].replace("Ширина", ";Ширина;")
            item['wrap-param'] = item['wrap-param'].replace("Глубина", ";Глубина;")
            item['wrap-param'] = item['wrap-param'].replace("Качество воды", ";Качество воды;")
            item['wrap-param'] = item['wrap-param'].replace("Максимально допустимое давление в корпусе насоса", ";Максимально допустимое давление в корпусе насоса;")

            item['wrap-param'] = item['wrap-param'].replace("Назначение", ";Назначение;")
            item['wrap-param'] = item['wrap-param'].replace("Качество воды", ";Качество воды;")
            item['wrap-param'] = item['wrap-param'].replace("Максимальный расход", ";Максимальный расход;")
            item['wrap-param'] = item['wrap-param'].replace("Максимальный напор", ";Максимальный напор;")
            item['wrap-param'] = item['wrap-param'].replace("Максимальная производительность", ";Максимальная производительность;")
            item['wrap-param'] = item['wrap-param'].replace("Максимальная глубина всасывания", ";Максимальная глубина всасывания;")

            item['wrap-param'] = item['wrap-param'].replace("Условный диаметр насоса", ";Условный диаметр насоса;")
            item['wrap-param'] = item['wrap-param'].replace("Диаметр выходного отверстия", ";Диаметр выходного отверстия;")
            item['wrap-param'] = item['wrap-param'].replace("Диаметр напорного патрубка", ";Диаметр напорного патрубка;")
            item['wrap-param'] = item['wrap-param'].replace("Режущий нож", ";Режущий нож;")
            item['wrap-param'] = item['wrap-param'].replace("Режим работы", ";Режим работы;")
            item['wrap-param'] = item['wrap-param'].replace("Номинальный диаметр присоединения DN", ";Номинальный диаметр присоединения DN;")

            item['wrap-param'] = item['wrap-param'].replace("Артикул производителя", ";Артикул производителя;")
            item['wrap-param'] = item['wrap-param'].replace("Гарантия", ";Гарантия;")
            item['wrap-param'] = item['wrap-param'].replace("Производитель", ";Производитель;")



            writer.writerow([item['title'], item['link_product'], item['img-product'], item['price'], item['wrap-param']])


def parser():

            PAGENATION = int(koltovara.strip())
            PAGENATION = PAGENATION + 1
            html = get_html(URL)
            if html.status_code == 200:
                cards = []
                for page in range(1, PAGENATION):
                    print(f'парсим страницу №{page}')
                    html = get_html(URL, params={'PAGEN_1': page})
                    cards.extend(get_content(html.text))
                    s_file(cards, CSV)
                print(f'всего спаршено {len(cards)}товаров')
            else:
                print('error')


parser()
