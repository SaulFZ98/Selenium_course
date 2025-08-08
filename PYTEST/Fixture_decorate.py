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
@pytest.fixture(scope='module')
def setup_login_uno():
    print("Empezando el login del sistema uno")
    yield
    print("saliendo del sistema prueba ok ")

@pytest.fixture(scope='module')
def setup_login_dos():
    print("empezando test del sistema dos")
    yield
    print("salidas del as pruebas dos ")

def test_uno(setup_login_uno):
    print("empezando las pruebas del test uno")


def test_dos(setup_login_dos):
    print("haciendo test dos ")


@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("preba tres del modulo dos ")