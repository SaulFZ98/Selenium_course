import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()

driver.get("https://www.adidas.mx/")
driver.maximize_window()
#driver.implicitly_wait(10)
t=6

element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='glass-gdpr-default-consent-accept-button']")))
element.click()
#driver.find_element(By.XPATH,"//button[@id='glass-gdpr-default-consent-accept-button']").click()


driver.find_element(By.XPATH,"//input[contains(@data-auto-id,'searchinput-desktop')]").send_keys("tenis")


time.sleep(t)
driver.close()