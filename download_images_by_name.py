import requests as r
from fake_useragent import UserAgent
import img2pdf
from config import url_math

user = UserAgent().random
header = {'User-Agent': user}

images = []

for i in range(1, 145):
    url = f'{url_math}{i:03d}.jpg'
    download = r.get(url, headers=header).content

    images.append(download)
    print(f'{i} images downloaded')

# Створюємо PDF з усіх зображень
with open('result.pdf', 'wb') as f:
    f.write(img2pdf.convert(images))