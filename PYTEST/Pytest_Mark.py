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
def test_uno():
    print("test 1")

@pytest.mark.run
def test_dos():
    print("test 2")

@pytest.mark.tres
def test_tres():
    print("test 3")

@pytest.mark.cuatro
def test_cuatro():
    print("test 4")
