import requests as r
from fake_useragent import UserAgent
import img2pdf

user = UserAgent().random
header = {'User-Agent': user}

images = []

with open('pages.txt', 'r') as file:
    for num, page in enumerate(file, start=1):
        download = r.get(page.strip(), headers=header).content
        images.append(download)
        print(f'{num} images downloaded')

# Створюємо PDF з усіх зображень
with open('result.pdf', 'wb') as f:
    f.write(img2pdf.convert(images))