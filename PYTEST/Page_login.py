import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from Funciones import Funciones_global


class Funciones_Login():

    def __init__(self,driver):
        self.driver = driver


    def L1(self,email,clave, message,t=1):
        global driver
        driver = webdriver.Firefox()
        f = Funciones_global(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        driver.maximize_window()
        f.texto_mixto("xpath", "//input[contains(@name,'username')]", email, 2)
        f.texto_mixto("xpath", "//input[contains(@type,'password')]", clave, 2)
        f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", 2)
        e1 = f.SEX("//p[contains(@class,'oxd-text oxd-text--p oxd-alert-content-text')]", )
        e1 = e1.text
        # print(e1)
        if e1 == message:
            print("la prueba de validacion exitosa")
        else:
            print("La prueba de validacion es incorrecta")
        driver.close()



    def L2(self,email,clave,message,t=3):
        global driver
        driver = webdriver.Firefox()
        f = Funciones_global(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        driver.maximize_window()
        f.texto_mixto("xpath", "//input[contains(@name,'username')]", email, 2)
        f.texto_mixto("xpath", "//input[contains(@type,'password')]", clave, 2)
        f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", 2)
        e1 = f.SEX("//span[contains(@class,'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message')]", )
        e1 = e1.text
        # print(e1)

        if e1 == message:
            print("la prueba de validacion exitosa")
        else:
            print("La prueba de validacion es incorrecta")
        driver.close()


    def L3(self,mail,clave,message,t=3):
        global driver
        driver = webdriver.Firefox()
        f = Funciones_global(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 2)
        driver.maximize_window()
        f.texto_mixto("xpath", "//input[contains(@name,'username')]", mail, 2)
        f.texto_mixto("xpath", "//input[contains(@type,'password')]", clave, 2)
        f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", 2)
        e1 = f.SEX("//a[@href='/web/index.php/admin/viewAdminModule']", )
        e1 = e1.text
        print(e1)
        if e1 == message:
            print("la prueba login de validacion exitosa")
        else:
            print("La prueba login de validacion es incorrecta")
        driver.close()
