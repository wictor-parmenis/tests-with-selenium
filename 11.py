from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_05_b.html'

browser.get(url)
#titulo = browser.find_element_by_class_name('topico')
linguagens = browser.find_elements_by_class_name('linguagens')
for linguagem in linguagens:
    print(
        (linguagem.find_element_by_tag_name('h2').text,
        linguagem.find_element_by_tag_name('p').text)
    )