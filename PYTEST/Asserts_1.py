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
    dato = "Computadora"
    frase ="dentro de las computadoras hay memoria Ram"

    assert  dato in frase, "El dato no esta dentro de la frase"