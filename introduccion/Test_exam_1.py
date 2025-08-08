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


driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
t=4
try:
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@name,'firstname')]")))
    element = driver.find_element(By.XPATH, "//input[contains(@name,'firstname')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(t)
    element.send_keys("saul" + Keys.TAB, "test")
    element_1 = driver.find_element(By.XPATH,"//input[contains(@id,'sex-0')]").click()
    element_2 = driver.find_element(By.XPATH, "//input[contains(@id,'exp-3')]").click()
    element_3 = driver.find_element(By.XPATH, "//input[contains(@id,'datepicker')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", element_3)
    element_3.send_keys("10/02/2025")
    element_4 = driver.find_element(By.XPATH,"//input[contains(@id,'profession-1')]").click()
    element_5 = driver.find_element(By.XPATH, "//input[contains(@id,'tool-2')]").click()
    element_6 = driver.find_element(By.XPATH, "//select[contains(@id,'continents')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", element_6)
    conti = Select(element_6)
    conti.select_by_visible_text("North America")
    element_7 = driver.find_element(By.XPATH, "//option[contains(.,'WebElement Commands')]")
    element_7.send_keys("Wait Commands")
    element_7.send_keys("C://Users//saul.frias//PycharmProjects//SeleniumProject//introduccion//imagen//pega.png")

except TimeoutException as ex:
    print(ex.msg)
time.sleep(t)


driver.close()


