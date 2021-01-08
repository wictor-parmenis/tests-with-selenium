from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)
sleep(4)
name = browser.find_element_by_css_selector('[type= "text"]')
senha = browser.find_element_by_css_selector('[type = "password"]')
btn = browser.find_eSlement_by_css_selector('[type = "submit"]')

name.send_keys('Wictor')
senha.send_keys('123')
btn.click()


'''
Query: https://selenium.dunossauro.live/aula_06_a.html?nome=Wictor&senha=123&l0c0=Enviar%21#
'''