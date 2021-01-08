from selenium.webdriver import Firefox
from json import loads
from time import sleep
from urllib.parse import urlparse

browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_04.html'

browser.get(url)
sleep(4)

def preenche(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

structure = {
    'nome' : 'José Wictor',
    'email' : 'wictortec@gmail.com',
    'senha' : '123456',
    'telefone' : '1232323232'
}

preenche(browser, **structure)

result = browser.find_element_by_tag_name('textarea').text
result_new = result.replace('\'', "\"").replace('+', ' ')
assert structure == loads(result_new)
