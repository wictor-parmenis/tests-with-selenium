from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'http://selenium.dunossauro.live/aula_04_a.html'

browser.get(url)
sleep(4)
ul = browser.find_elements_by_tag_name('ul')

li = ul[0].find_elements_by_tag_name('li')
a = li[0].find_elements_by_tag_name('a')
print(a[0].text)
