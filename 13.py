from selenium.webdriver import Firefox
from json import loads
from time import sleep
from urllib.parse import urlparse

browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_04.html'

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

browser.get(url)
sleep(4)
struture = {
    'nome' : 'José Wictor',
    'email' : 'wictortec@gmail.com',
    'senha' : 'dados123',
    'telefone' : '987423260'
}
preenche_form(browser, **struture)

url_parseada = urlparse(browser.current_url).query
url_parseada2 = url_parseada.split('&')

one = url_parseada2[0].replace('nome=', "")
two = one.replace('%C3%A9', "é")
three = two.replace('+', " ")
name_right = three.replace('\'', "\"")

five = url_parseada2[1].replace('email=', "")
six = five.replace('%40', "@")
email_right = six.replace('\'', "\"")

eight = url_parseada2[2].replace('senha=', "")
password_right = eight.replace('\'', "\"")

ten = url_parseada2[3].replace('telefone=', "")
phone_right = ten.replace('\'', "\"")

dict_results = {}
dict_results = {'nome' : name_right, 'email' : email_right, 'senha' : password_right, 'telefone' : phone_right}
print(dict_results)



'''
Query da Url:
nome=Jos%C3%A9+Wictor
&
email=wictortec%40gmail.com
&
senha=dados123
&
telefone=987423260
&
btn=Enviar%21
'''