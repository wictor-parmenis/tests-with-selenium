from selenium.webdriver import Chrome
from time import sleep
import re

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep(5)
a = browser.find_element_by_tag_name('a')
while True:
    a.click()
    p = browser.find_elements_by_tag_name('p')
    p1 = p[-1].text
    if re.search('\\bVocê ganhou\\b', p1, re.IGNORECASE):
        break
    

'''
while True:
    a.click()
    p = browser.find_elements_by_tag_name('p')
    print(p[-1].text)
    if p[-1].text == 'você está fazendo algo errado':
        break
'''