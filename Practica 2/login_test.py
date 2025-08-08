import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert



class login_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


        t = 3
    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("saul")
        passw.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        error = error.text
        #print(error)
        if (error=="Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos")
            print("prueba 1")

        time.sleep(5)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("")
        passw.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if (error=="Epic sadface: Username is required"):
            print("el nombre no esta ")
            print("prueba 2")
            time.sleep(5)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("saul")
        passw.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        error = error.text
        #print(error)
        if (error=="Epic sadface: Password is required"):
            print("el password no esta ")
            print("prueba 3")
            time.sleep(5)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("")
        passw.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if (error=="Epic sadface: Username is required"):
            print("el password no esta ")
            print("prueba 4")
            time.sleep(5)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        passw.send_keys("secret_sauce")
        btn.click()

        elemento = driver.find_element(By.XPATH, "//div[contains(@class,'app_logo')]")
        elemento.is_displayed()
        print("el elemento es:" + str(elemento))

        '''
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if (error=="Epic sadface: Username is required"):
            print("el password no esta ")
            print("prueba 4")


        '''
        time.sleep(5)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()