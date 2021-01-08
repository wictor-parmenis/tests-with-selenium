from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

browser = Firefox()
url = 'https://selenium.dunossauro.live/aula_05.html'

browser.get(url)
sleep(4)

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

sleep(4)

estrutura = {
    'nome' : 'José Wictor',
    'email' : 'wictortec@gmail.com',
    'senha' : '123456',
    'telefone' : '87423260'
}

preenche_form(browser, **estrutura)
sleep(4)
texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")
resultado_arrumado2 = resultado_arrumado.replace('+', " ")
dic_results = loads(resultado_arrumado2)

assert dic_results == estrutura


#? Query String
'''
https://selenium.dunossauro.live/aula_05.html
?
nome=Jos%C3%A9+Wictor
&
email=wictortec%40gmail.com
&
senha=123456
&
telefone=74646464
&
btn=Enviar%21#
'''