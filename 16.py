from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

browser = Firefox()
url = 'https://selenium.dunossauro.live/aula_05.html'

structure = {
    'nome' : 'Wictor',
    'email' : 'wictortec@gmail.com',
    'senha' : 'slackware',
    'telefone' : '991021317'
}

browser.get(url)
sleep(6)
def preenche_forms(nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


preenche_forms(**structure)
#url_parseada = urlparse(browser.current_url)
sleep(6)
texto_resultado = browser.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_results = loads(resultado_arrumado)
assert dic_results == structure

browser.quit()



