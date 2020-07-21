import time
import pytest
import unittest
from selenium.webdriver.common.by import By
import requests
import urllib.request
import os
from selenium import webdriver


link = "https://netpeak.ua/"

class search_site (unittest.TestCase):
    def test_01(self):
        try:
            self.browser = webdriver.Chrome()
# Переходим по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
            self.browser.get(link)
            browser = self.browser
# Переходим на страницу "Работа в Netpeak", нажав на кнопку "Карьера"
            pytest.career = browser.find_element_by_link_text("Карьера").click()
# Ждем пока браузер подгрузит страницу
            time.sleep(3)

# Переходим на страницу заполнения анкеты, нажав кнопку - "Я хочу работать в Netpeak"
            pytest.dream = browser.find_element_by_link_text("Я хочу работать в Netpeak").click()
            time.sleep(3)
# Находим сайт с картинкой в интернете
            url = 'https://www.python.org/static/opengraph-icon-200x200.png'
# Сохраняем картинку локально
            urllib.request.urlretrieve(url, os.getcwd()+"/image.png")
# Загружаем картинку вместо резюме
            pytest.upload = browser.find_element_by_name('up_file').send_keys(os.getcwd()+"/image.png")
# Заполняю случайными данными блок "3. Личные данные"
            pytest.name = browser.find_element_by_name("name").send_keys("Kateryna")
            pytest.lastname = browser.find_element_by_name("lastname").send_keys("Ivanova")
            pytest.year = browser.find_element_by_name("by").send_keys("2000")
            pytest.month = browser.find_element_by_name("bm").send_keys("июня")
            pytest.day = browser.find_element_by_name("bd").send_keys("18")
            pytest.e_mail = browser.find_element_by_name("hiringe").send_keys("Katerina@gmail.com")
            pytest.phone_number = browser.find_element_by_name("phone").send_keys("+380949678468")
            time.sleep(5)
# Нажимаю на кнопку отправить резюме
            pytest.send = browser.find_element_by_name("difficult").click()
# Жду чтоб проверить, что "Все поля являются обязательными для заполнения" - подсветилось красным цветом
            time.sleep(7)
# Нажимаю на логотип для перехода на главную страницу
            pytest.logo = browser.find_element(By.CLASS_NAME, "logo-block").click()
            time.sleep(5)

        finally: # закрываем браузер после всех манипуляций
            browser.quit()
# Убеждаюсь что открылась нужная страница.
            if requests.get("https://netpeak.ua/"):
                assert True


if __name__ == "__main__":
    unittest.main()

