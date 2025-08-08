import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()

driver.get("https://syntaxprojects.com/basic-select-dropdown-demo.php")
driver.maximize_window()
driver.implicitly_wait(10)
t=4

#days=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))
daysSelect=driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")

ds=Select(daysSelect)

ds.select_by_visible_text("Sunday")
time.sleep(t)

ds.select_by_index(3)
time.sleep(t)

ds.select_by_value("Friday")


city=Select(driver.find_element(By.ID, "multi-select"))
city.select_by_index(1)
time.sleep(t)
city.select_by_index(2)
time.sleep(t)
city.select_by_index(3)
time.sleep(t)

time.sleep(t)
driver.close()