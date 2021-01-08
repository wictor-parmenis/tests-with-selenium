from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Chrome()
browser.get(url)
sleep(6)
a = browser.find_element_by_tag_name('a')


def ten():
    i = 0
    while i <= 9:
        p = browser.find_elements_by_tag_name('p')
        a.click()
        print(f'Value element p: {p[-1].text} . Value of element "Click": {i}.')
        print(f'Os valores são iguais: {p[-1].text == str(i)}')
        i += 1

ten()


