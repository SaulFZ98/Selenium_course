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
        f.Navegar("https://www.google.com.mx/?hl=es-419",t)

        f.texto_mixto("xpath","//textarea[contains(@id,'APjFqb')]","ferrari",t)
        f.Click_XY("xpath","//textarea[contains(@id,'APjFqb')]",0,100,t)





    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ =='__main':
    unittest.main()