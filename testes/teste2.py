import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://10.11.12.123')
driver.maximize_window()
assert driver.title == "Cisco Systems Login"
driver.find_element_by_name("bSubmit ").click()
driver.save_screenshot('screenie.png')

driver.quit()
