from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Chrome()


def exe():
    browser.get(url)
    sleep(6)
    h1 = browser.find_element_by_tag_name('h1')
    dict_1 = {}
    dict_1 = {h1.text : 'vazio'}
    #print(dict_1)
    dict_2 = {}
    p = browser.find_elements_by_tag_name('p')
    for i in range(3):
        dict_2.update({f'texto{i+1}' : p[i].text})
        i += 1
    dict_3 = {h1.text : dict_2}
    print(dict_3)
    

exe()




