import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from Funciones import Funciones_global
from Page_login import Funciones_Login

t=5
driver = ""
f = ""

def setup_function(function):
    global driver, f
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    f = Funciones_global(driver)
    f.texto_mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.texto_mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("iniciando test")


def teardown_function(function):
    print("fin de los test")
    driver.close()


def test_uno():
    f = Funciones_global(driver)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    f.click_mixto("xpath", "//a[@href='/web/index.php/admin/viewAdminModule']", t)
    f.click_mixto("xpath","//span[contains(.,'Job')]",t)


def test_dos():
    f = Funciones_global(driver)
    f.click_mixto("xpath", "//a[@href='/web/index.php/admin/viewAdminModule']", t)
    f.click_mixto("xpath", "//span[contains(.,'Job')]", t)
    f.click_mixto("xpath","(//li[contains(.,'Job Titles')])[2]",t)
    f.click_mixto("xpath","//button[@class='oxd-button oxd-button--medium oxd-button--secondary']",5)
    time.sleep(4)


