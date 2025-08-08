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


#validacion ambas credenciales erroneas
def test_login1():
    driver = webdriver.Firefox()
    fl = Funciones_Login(driver)
    fl.L1("test@test.com","test","Invalid credentials")
    #validacion campo de user sin datos
    fl.L2("","test","Required")
    # validacion datos existosos
    fl.L3("Admin","admin123","Admin")


