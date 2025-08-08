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

@pytest.mark.validarif
def test_validar_if():
    a = 20
    b = 20
    if a==b :
       assert  True, "Los datos son iguales"
    else:
        assert False," no son iguales"
