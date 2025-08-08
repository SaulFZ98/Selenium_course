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

def get_Data():
    return[
        ("test1","test1"),
        ("test2", "test2"),
        ("test3", "test3"),
        ("test4", "test4"),
        ("Admin", "admin123")
    ]


@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
    global driver, f
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    f = Funciones_global(driver)
    f.texto_mixto("xpath", "//input[contains(@name,'username')]", user, t)
    f.texto_mixto("xpath", "//input[contains(@type,'password')]", clave, t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("entrando al sistema")


def teardown_funtion():
    print("salda del test")
    driver.close()
