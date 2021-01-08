from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys


browser = Chrome()
url = 'https://www.siga.ufrpe.br/ufrpe/index.jsp'

browser.get(url)
sleep(4)
cpf = browser.find_element_by_name('cpf')
cpf.send_keys('70561124477')
senha = browser.find_element_by_name('txtPassword')
senha.send_keys('#Deadpoll29')
enter = browser.find_element_by_id('btnEntrar')
enter.click()
sleep(4)
browser.find_element_by_id("complete2").send_keys('deta')
sleep(4)
browser.find_element_by_id('complete2').send_keys(Keys.DOWN)
sleep(4)
browser.find_element_by_id('complete2').send_keys(Keys.RETURN)




'''
<a href="#" id="menuTopo:repeatAcessoMenu:2:repeatSuperTransacoesSuperMenu:0:linkSuperTransacaoSuperMenu" name="menuTopo:repeatAcessoMenu:2:repeatSuperTransacoesSuperMenu:0:linkSuperTransacaoSuperMenu" onclick="A4J.AJAX.Submit('menuTopo',event,{'oncomplete':function(request,event,data){verificarTransacoes();},'similarityGroupingId':'menuTopo:repeatAcessoMenu:2:repeatSuperTransacoesSuperMenu:0:linkSuperTransacaoSuperMenu','parameters':{'menuTopo:repeatAcessoMenu:2:repeatSuperTransacoesSuperMenu:0:linkSuperTransacaoSuperMenu':'menuTopo:repeatAcessoMenu:2:repeatSuperTransacoesSuperMenu:0:linkSuperTransacaoSuperMenu','exibirMenuLateral':'false','codigoSuperTransacaoSelecionada':261} ,'containerId':'j_id_jsp_1675146373_0'} );return false;">Detalhamento de Discente</a>
'''