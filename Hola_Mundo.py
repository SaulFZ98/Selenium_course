
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver= webdriver.Chrome()
driver= webdriver.Firefox()

driver.get("https://demoqa.com/text-box")

print(driver.title)

driver.close()