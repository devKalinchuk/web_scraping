from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent


user_agent = UserAgent()
url = 'INPUT_URL_HERE'
CHROME_DRIVER_PATH = "PATH_TO_CHROME_DRIVER"

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=" + user_agent.chrome)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)
driver.maximize_window()

try:
    driver.get(url)
    driver.execute_script("document.documentElement.style.scrollBehavior = 'smooth';")
    with open('url_pages.txt', 'w') as file:
        for i in range(1, 671):
            attempts = 0
            page_id = f"page{i}"
            driver.execute_script("window.scrollBy(0, 1200)")
            sleep(3)
            page = driver.find_element(By.ID, page_id)
            image = page.find_element(By.TAG_NAME, "img").get_attribute("src")
            while not image:
                attempts += 1
                if attempts >= 5:
                    print(f'Помилка на сторінці {i}')
                    exit()
                print(f'Не знайдено сторінку {i}, спроба {attempts}')
                driver.execute_script("window.scrollBy(0, 300)")
                sleep(3)
                page = driver.find_element(By.ID, page_id)
                image = page.find_element(By.TAG_NAME, "img").get_attribute("src")
            print(f'Сторінка {i} - {image}')
            file.write(image + '\n')
            file.flush()

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()