import  time

import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from  functions.Funciones import Funciones_global
from selenium.webdriver import ActionChains

t= 3

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        t= 2

    def test1(self):
        driver = self.driver
        f = Funciones_global(driver)
        f.Navegar("https://www.techlistic.com/p/selenium-practice-form.html#google_vignette",t)
        #f.texto_mixto("xpath","//input[contains(@name,'username')]","Admin",t)
        #f.texto_mixto("xpath","//input[contains(@type,'password')]","admin123",t)
        #f.click_mixto("xpath","//button[contains(@type,'submit')]",t)


        categoria = driver.find_element(By.XPATH, "(//a[@class='dropbtn'][contains(.,'Selenium')])[1]")
        sub1 = driver.find_element(By.XPATH,"(//a[@href='https://www.techlistic.com/p/selenium-with-python-tutorial.html'][contains(.,'Selenium with Python Tutorial')])[1]")
        #sub2 = driver.find_element(By.XPATH, "(//li[contains(.,'Users')])[2]")

        act = ActionChains(driver)
        act.move_to_element(categoria).move_to_element(sub1).click().perform()

        time.sleep(4)



    def tearDown(self):
        driver = self.driver
        driver.close()
