import time
import re
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Variaveis de acesso

proto = "https"
url = "172.16.165.10"
username = "admin"
password = "Admin123"
delay = 0

# Variaveis do Script

img = 1
fullurl = proto + '://' + username + ':' + password + '@' + url
modulo = 'Monitor'

# Define as funcoes

def screencap(Text, number):
    Text = gettext(Text)
    filename = modulo + '-' + str(number).zfill(3) + '-' + driver.title + '-' + Text + '.png'
    number += 1
    getscrollsize()
    time.sleep(delay)
    driver.save_screenshot(filename)
    driver.maximize_window()

    return number

def gettext(Text):
    toremove = re.compile('<.*?>')
    Text = re.sub(toremove, '', Text)
    Text = re.sub('\n', '', Text)
    Text = re.sub('/', '_', Text)
    Text = Text.lstrip()
    Text = re.sub(' ', '_', Text)
    
    return Text

def getscrollsize():

    driver.switch_to.default_content()

    actual_size = driver.get_window_size()

    actual_height = actual_size['height']
    actual_width = actual_size['width']

    navBar = driver.find_element_by_name('mainFrame')
    driver.switch_to.frame(navBar)

    navBar = driver.find_element_by_name('content')
    driver.switch_to.frame(navBar)
    
    new_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    new_height += 63
    new_width  = driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
    new_width  += 180
    
    if new_height < actual_height: new_height = actual_height
    if new_width < actual_width: new_width = actual_width

    if new_height != actual_height or new_width != actual_width:
        #driver.manage.window.resize_to(new_width, new_height)
        driver.set_window_size(800, 600)
        #driver.set_window_rect(x=-1000, y=-1000, width=new_width, height=new_height)
        driver.set_window_position(-1000,-1000)
        driver.set_window_size(new_width, new_height)
    driver.switch_to.default_content()

    navBar = driver.find_element_by_name('mainFrame')
    driver.switch_to.frame(navBar)

    navBar = driver.find_element_by_name('navBar')
    driver.switch_to.frame(navBar)

    return None

driver = webdriver.Chrome()

# Carrega a URL do WLC passando usuario e senha
# para evitar o PopUp de autenticacao

driver.get(fullurl)

# Maximiza a janela do Chrome
# e garante que estamos na pagina correta

actual_size = driver.get_window_size()

print('height: ' + str(actual_size['height']))
print('width: ' + str(actual_size['width']))

#print(driver.get_window_size())
# {'height': 1033, 'width': 945}
driver.maximize_window()

actual_size = driver.get_window_size()

print('height: ' + str(actual_size['height']))
print('width: ' + str(actual_size['width']))

#print(driver.get_window_size())
# {'height': 1053, 'width': 1920}
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
        img = screencap(html, img)

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