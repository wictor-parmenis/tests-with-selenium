from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://umusicomelhor.com/wp-admin/'

browser.get(url)
sleep(4)

login = browser.find_element_by_name('log')
login.send_keys('umusicomelhor')
password = browser.find_element_by_name('pwd')
password.send_keys('#Deadpoll29')
sleep(2)
button1 = browser.find_element_by_name('wp-submit')
button1.click()

