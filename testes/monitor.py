import time
import re
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Variaveis de acesso

proto = "https"
url = "10.11.12.123"
username = "admin"
password = "Admin123"
delay = 0

# Variaveis do Script

img = 1
fullurl = proto + '://' + username + ':' + password + '@' + url
modulo = 'Monitor'

# Define as funcoes

def screencap(Text, number):
    filename = modulo + '-' + str(number).zfill(3) + '-' + driver.title + '-' + Text + '.png'
    number += 1
    time.sleep(delay)
    driver.save_screenshot(filename)

    return number

def gettext(Text):
    toremove = re.compile('<.*?>')
    Text = re.sub(toremove, '', Text)
    Text = re.sub('\n', '', Text)
    Text = re.sub('/', '_', Text)
    Text = Text.lstrip()
    Text = re.sub(' ', '_', Text)
    
    return Text

# Carrega o Webdriver chamando uma instancia do Chrome

driver = webdriver.Chrome()

# Carrega a URL do WLC passando usuario e senha
# para evitar o PopUp de autenticacao

driver.get(fullurl)

# Maximiza a janela do Chrome
# e garante que estamos na pagina correta

driver.maximize_window()
assert driver.title == 'Cisco Systems Login'

# Efetua o click no Botao Login

driver.find_element_by_name('bSubmit ').click()

# Recarrega a pagina principal para corrigir
# problemas com os elementos visuais

driver.get(proto + '://' + url + '/screens/frameset.html')

# Move para o Frame da Esquerda

navBar = driver.find_element_by_name('mainFrame')
driver.switch_to.frame(navBar)

navBar = driver.find_element_by_name('navBar')
driver.switch_to.frame(navBar)

# Econtra os elementos do menu e define o tamanho dos arrays

navBar1 = driver.find_elements_by_class_name('navBar1')
navBar2 = driver.find_elements_by_class_name('navBar2')

navBar1_max = len(navBar1) - 1
navBar1_id = 0
navBar2_max = len(navBar2) - 1
navBar2_id = 0

# Entra e captura a primeira opcao do primeiro nivel do menu

navBar1[navBar1_id].click()
img = screencap(navBar1[navBar1_id].text, img)

# Entra e captura da segunda opcao do primeiro nivel em diante
# e captura as opcoes do segundo nivel

for menu in navBar2:
    html = str(menu.get_attribute('outerHTML'))
    
    if 'selectLink(this)' in html:
        if not menu.is_displayed():
            navBar1[navBar1_id].click()
            navBar1_id += 1
            navBar1[navBar1_id].click()

        menu.click()
        menu_name = gettext(html)
        img = screencap(menu_name, img)

    navBar2_id += 1

navBar1[navBar1_id].click()
navBar1_id += 1

# Trata as demais opcoes level 1 do menu

while not navBar1_id > navBar1_max:

    if not navBar1[navBar1_id].is_displayed():
        navBar1_id += 1

    else:
        navBar1[navBar1_id].click()
        
        try:
            driver.switch_to.alert.accept()
        
        except NoAlertPresentException:
            pass

        img = screencap(navBar1[navBar1_id].text, img)
        navBar1_id += 1

driver.quit()