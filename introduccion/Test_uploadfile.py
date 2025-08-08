import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#investigar como se hace en firefox ya que da problema la ruta de la imagen, en chrome funciona bien

driver=webdriver.Chrome()

driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.maximize_window()
#driver.implicitly_wait(10)
t=4



try:
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    element= driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    element.send_keys("C://Users//saul.frias//PycharmProjects//SeleniumProject//introduccion//imagen//pega.png")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)




time.sleep(t)
driver.close()