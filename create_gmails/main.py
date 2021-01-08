from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-n-en&flowName=GlifWebSignIn&flowEntry=SignUp'

browser.get(url)
sleep(4)

name = browser.find_element_by_id('firstName')
lname = browser.find_element_by_id('lastName')
username = browser.find_element_by_id('username')
pwd = browser.find_element_by_name('Passwd')
pwd_repeat = browser.find_element_by_name('ConfirmPasswd')
button1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')

strucuture = {
'nome' : 'Josenaldo',
'lnome' : 'Putaquepariu',
'login' : 'josenaldolulaldo',
'senha' : 'xerebenebia',
'repeat_senha' : 'xerebenebia'
}


sleep(4)
def CreateGmail(nome, lnome, login, senha, repeat_senha):
    name.send_keys(nome)
    lname.send_keys(lnome)
    username.send_keys(login)
    pwd.send_keys(senha)
    pwd_repeat.send_keys(repeat_senha)
    button1.click()


CreateGmail(**strucuture)




