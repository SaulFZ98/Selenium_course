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

@pytest.mark.run
def test_validar_if():
    print("Primer test")
    assert  True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b, "no son iguales"
    assert a!=b, "son iguales"
    assert a<b,"A no es mnor que b"
    assert a>b,"a no es menor que b"

@pytest.mark.run
def test_tres():
    a=5
    b=10
    assert a==b, "no son iguales"

@pytest.mark.run
def test_cuatro():
    a=15
    b=10
    assert a>b, "A no son mayor que b"


@pytest.mark.run
def test_cinco():
    nom="test"
    assert nom=="adsad", "A no son mayor que b"