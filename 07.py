from selenium.webdriver import Chrome
from time import sleep

class one:
    browser = Chrome()

    def __init__(self):
        self.browser.get('http://selenium.dunossauro.live/aula_04_b.html')

    @staticmethod
    def find_for_text(browser, tag, text):
    elements = browser.find_elements_by_tag_name(tag) #list
    for element in elements:
        if element.text == text:
            return element
    return
        

if __name__ == "__main__":
    one()

    
