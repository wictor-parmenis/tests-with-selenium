from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')

def find_for_text(browser, tag, text):
    elements = browser.find_elements_by_tag_name(tag) #list
    for element in elements:
        if element.text == text:
            return element
    return
numbers = ['um', 'dois', 'tres', 'quatro']

for n in numbers:
    find_for_text(browser, 'div', n).click()

for n in numbers:
    browser.back()
    sleep(0.3)

for n in numbers:
    browser.forward()
    sleep(0.3)