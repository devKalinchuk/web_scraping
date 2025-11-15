import requests as r
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import img2pdf
from PIL import Image
from io import BytesIO

user = UserAgent().random
header = {'User-Agent': user}

html = 'INPUT_URL_HERE'
images = []
target_width = 1200

for i in range(1, 15):
    url = f'{html}/{i}/'
    web = r.get(url, headers=header).text
    bs = BeautifulSoup(web, 'lxml')
    image = bs.find('div', class_='photo mb-4').find('img', class_='img-fluid').attrs['src']
    image = 'html' + image
    download = r.get(image, headers=header).content

    image_path = f'image_{i}.jpg'
    # Відкриваємо зображення через PIL
    img = Image.open(BytesIO(download))

    # Змінюємо розмір зі збереженням пропорцій
    aspect_ratio = img.height / img.width
    target_height = int(target_width * aspect_ratio)
    img_resized = img.resize((target_width, target_height), Image.LANCZOS)

    # Зберігаємо змінене зображення
    img_resized.save(image_path, 'JPEG', quality=95)

    # Додаємо шлях до списку
    images.append(image_path)
    print(f'{i} images downloaded')

# Створюємо PDF з усіх зображень
with open('answers/result.pdf', 'wb') as f:
    f.write(img2pdf.convert(images))