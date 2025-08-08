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
        f.Navegar("https://demoqa.com/automation-practice-form#google_vignette",t)

        f.texto_mixto("xpath","//input[contains(@id,'firstName')]","test",t)

        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(3)
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(3)
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys("gmail.com").perform()
        time.sleep(3)





    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ =='__main':
    unittest.main()