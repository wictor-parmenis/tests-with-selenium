from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

sleep(4)

def find_for_text(browser, tag, text):
    '''
    varredura de elementos de um site.
    Argumentos = browser = navegador();
                 tag do site;
                 texto a ser procurado.
    '''
    elements = browser.find_elements_by_tag_name(tag) #list
    for element in elements:
        if element.text == text:
            return element
    return


element_ddg = find_for_text(browser, 'a', 'DuckDuckGo')


