from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent


user_agent = UserAgent()
url = 'https://www.scribd.com/document/724064011/%D0%A1%D1%82%D0%B8%D0%B2%D0%B5%D0%BD%D1%81-%D0%9F%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B-tcp-ip-%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5-%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE#page=1'
CHROME_DRIVER_PATH = "/home/nicolas/.wdm/drivers/chromedriver/linux64/142.0.7444.61/chromedriver-linux64/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=" + user_agent.chrome)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)
driver.maximize_window()

try:
    driver.get(url)
    driver.execute_script("document.documentElement.style.scrollBehavior = 'smooth';")
    with open('pages.txt', 'w') as file:
        for i in range(1, 671):
            attemts = 0
            page_id = f"page{i}"
            driver.execute_script("window.scrollBy(0, 1200)")
            sleep(3)
            page = driver.find_element(By.ID, page_id)
            image = page.find_element(By.TAG_NAME, "img").get_attribute("src")
            while not image:
                attemts += 1
                if attemts >= 5:
                    print(f'Помилка на сторінці {i}')
                    exit()
                print(f'Не знайдено сторінку {i}, спроба {attemts}')
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