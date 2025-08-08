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
        #f.Navegar("https://demo.automationtesting.in/Static.html",t)
        #f.Drag_Drop("xpath","(//img[@src='logo.png'])[1]","//div[contains(@id,'droparea')]",3)

        #drag and drop x y

        f.Navegar("https://jqueryui.com/draggable/",t)
        f.Drag_DropXY("xpath","//div[contains(@id,'draggable')]",150,180,t)




    def tearDown(self):
        driver = self.driver
        driver.close()