import time
from selenium import webdriver

img = 1

# Carrega o Webdriver chamando uma instância do Chrome

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# Carrega a URL do WLC passando usuário e senha
# para evitar o PopUp de autenticação

driver.get('https://admin:Admin123@10.11.12.123')

# Maximiza a janela do Chrome
# e garante que estamos na página correta

driver.maximize_window()
assert driver.title == 'Cisco Systems Login'

# Efetua o click no Botão Login

driver.find_element_by_name('bSubmit ').click()

# Recarrega a página principal para corrigir
# problemas com os elementos visuais

driver.get('https://10.11.12.123'+'/screens/frameset.html')

# Fefetua o Screenshot e incrementa o contador
### ToDo: Transformar em Função

driver.save_screenshot('monitor-'+str(img).zfill(2)+'.png')
img += 1

print(str(img).zfill(2))

#### Não modificar acima está "OK?!?!?"

navBar = driver.find_element_by_name('mainFrame')
print(driver.title)
driver.switch_to.frame(navBar)
print(driver.title)
navBar = driver.find_element_by_name('navBar')
driver.switch_to.frame(navBar)
print(driver.title)
menu = driver.find_element_by_link_text('Access Points')
print(menu)
menu.click()
menu = driver.find_element_by_link_text('802.11a/n/ac')
menu.click()

# Fefetua o Screenshot e incrementa o contador
### ToDo: Transformar em Função

driver.save_screenshot('monitor-'+str(img).zfill(2)+'.png')
img += 1

print(str(img).zfill(2))

menu = driver.find_element_by_link_text('802.11b/g/n')
menu.click()

# Fefetua o Screenshot e incrementa o contador
### ToDo: Transformar em Função

driver.save_screenshot('monitor-'+str(img).zfill(2)+'.png')
img += 1

print(str(img).zfill(2))

menu = driver.find_element_by_link_text('Dual-Band Radios')
menu.click()

# Fefetua o Screenshot e incrementa o contador
### ToDo: Transformar em Função

driver.save_screenshot('monitor-'+str(img).zfill(2)+'.png')
img += 1

print(str(img).zfill(2))

driver.quit()
