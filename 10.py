from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_04.html'
browser.get(url)
sleep(4)
a1 = browser.find_elements_by_tag_name('a')
a1[-15].click()
