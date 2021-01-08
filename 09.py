from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_04.html'
browser.get(url)
sleep(4)
print(len(browser.find_elements_by_tag_name('a')))
aside = browser.find_element_by_tag_name('aside')
links = aside.find_elements_by_tag_name('a')
dicio = {}
for link in links:
    dicio[link.text] = link.get_attribute('href')

pprint(dicio)
    

