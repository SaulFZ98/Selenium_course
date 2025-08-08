import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#investigar como se hace en firefox ya que da problema la ruta de la imagen, en chrome funciona bien

driver=webdriver.Firefox()

driver.get("https://pixabay.com/es/")
driver.maximize_window()
#driver.implicitly_wait(10)
t=4


#driver.execute_script("window.scrollTo(0,100)")


try:
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec']")))
    element = driver.find_element(By.XPATH, "//a[@href='/es/images/search/?order=ec']")
    ir = driver.execute_script("arguments[0].scrollIntoView();",element)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)



time.sleep(t)
driver.close()