import time
from xml.dom.xmlbuilder import Options

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import  Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()


driver.get("https://syntaxprojects.com/basic-select-dropdown-demo.php")
driver.maximize_window()
t=4
#obteniendo todos los links d ela pagina

links = driver.find_elements(By.TAG_NAME, "a")
print("el numero de links que hay en la pagina es: ", len(links))

for num in links:
    print(num.text)


driver.find_element(By.LINK_TEXT, "All Locators").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Locators").click()
time.sleep(t)


driver.close()


