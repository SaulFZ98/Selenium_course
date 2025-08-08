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

t=3

@pytest.fixture(scope='module')
def setup_login():
    global driver, f
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_global(driver)
    f.texto_mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.texto_mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("entrando al sistema")

def teardown_function():
    print("fin de los test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
    title =f.SEX("//h6[contains(.,'Dashboard')]").text
    print(title)
    if title== "Dashboard":
        print("Estas en la paguina de inicio")
        assert title=="Dashboard"
    else:
        assert title !="Dashboard", "no pudiste entrar al sistema"
