import time
import unittest
import  os

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from functions.Funciones import  Funciones_global
from functions.Page_login import Pagina_login
from selenium.webdriver.firefox.service import Service



t=6

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        t = 3

    def test1(self):
        driver = self.driver
        f = Funciones_global(driver)
        #pg = Pagina_login(driver)
        #pg.Login_master("https://www.saucedemo.com/v1/", "saul","admin", t)
        #f.Navegar("https://syntaxprojects.com/basic-select-dropdown-demo.php", t)
        #f.Select_xpath_text("//select[contains(@id,'select-demo')]", "Sunday", t)
        #f.Select_xpath_type("//select[contains(@id,'select-demo')]","value","Sunday", t)
        #f.Select_ID_type("//select[contains(@id,'select-demo')]","index", "3", t)
        #f.Navegar("https://syntaxprojects.com/basic-checkbox-demo.php", t)
        #f.Upload_xpath_type("//input[contains(@id,'fileinput')]","C://Users//saul.frias//PycharmProjects//SeleniumProject//introduccion//imagen//pega.png",t)
        #f.Check_xpath_("//label[contains(.,'Option 1')]", t)
        #for n in range (2,4):
         #   f.Check_xpath_multiples(6,"//input[contains(@value,'Option-"+str(n)+"')]" )
          #  print(n)
            #// input[contains( @ value, 'Option-2')]
        f.Navegar("https://demoqa.com/text-box#google_vignette",t)
        f.texto_mixto("id","userName","test", t)
        f.click_mixto("id","submit", t)

        f.Salida()




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()
