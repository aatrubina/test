import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from OnlineShop.models import Product

def parse_yandex_market(category_url):
    response = requests.get(category_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='n-snippet-card')

        for product in products:
            name = product.find('div', class_='n-snippet-card2__title').text.strip()
            image_url = product.find('img', class_='image').get('src')
            content = product.find('div', class_='n-snippet-card2__desc').text.strip()
            price = product.find('span', class_='price').text.strip()

            existing_product = Product.objects.filter(name=name).first()

            if existing_product:
                print(f"Товар с названием {name} уже существует, пропускаем...")
                continue
            image_content = requests.get(image_url).content
            product_image = ContentFile(image_content, name=f"{name}.jpg")
            product = Product.objects.create(name=name, image=product_image, content=content, price=price)
            print(f"Товар '{name}' успешно добавлен")

        print('Данные о товарах успешно сохранены в базе данных')

    else:
        print('Ошибка при отправке запроса:', response.status_code)

category_url = 'https://market.yandex.ru/catalog--tovary-dlia-koshek/62806/list?hid=90813&rs=eJwz6mUOYDzKyMCQZgskF1RZA0mHFzZAMuH9bhCbDyTS0AESOcABIhXqwOJ9IPEHG0EiD_pA5AKJPSBzILKPwSK7wextIHaDPlh2J0jkwUUQu8EaRDoEguxV0Aar8QPLngazwboYFliA1DCA1awDu-o-2N7q_SDZPTtApAVYPBRMrgWb7AH2CwuIbOAEkQ_qwWwfsBt-g81XA7utCezfMrDIT7DvzoFIh81g2ZlgcSaQmgUrwD66DXbVd7AbnoBFwC5XEN8LIo3AofEHossGrotBGmzmQ7B_68HqHcAuuQy2xcr6FCNHSrJRUopxWqqTFZckFwcHowCjBKMCowCTFHtKalpiaU6JAoMGA5c0WEpBgleBRYBNihMqFW8EkhRgBAAQe5DR'

parse_yandex_market(category_url)
