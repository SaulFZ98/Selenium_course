import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


driver=webdriver.Firefox()
t=4

driver.get("https://adminlte.io/themes/v3/pages/UI/modals.html")
driver.maximize_window()

time.sleep(t)



try:
    driver.switch_to.alert.accept()  # ejecutar el boton aceptar
    driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Launch Default Modal')]").click()
    driver.find_element(By.XPATH, "(//button[@type='button'][contains(.,'Save changes')])[1]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("error en intento")



driver.close()


