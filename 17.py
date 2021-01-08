from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Chrome()

browser.get(url)
sleep(6)

structure = {
    'nome' : 'Wictor',
    'email' : 'wictortec@gmail.com',
    'senha' : 'slackware',
    'telefone' : 'telefone'
}

def preencher(nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

preencher(**structure)
sleep(4)
url_parseada = urlparse(browser.current_url)
#url_parseada.query.split('&')

url_resultado =  url_parseada.query.split('&')
url_arrumada = url_resultado.replace('\'', "\"").replace('%',"@")
url_resultado[1].replace(' = ', " : ")
print(url_resultado)