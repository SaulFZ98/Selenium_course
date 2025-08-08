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

def setup_function(function):
    print("esto va al inicio de cada test")

def teardown_function(function):
    print("esto va al final de cada test")


def test_uno():
    print("test uno")



def test_dos():
    print("test dos")


def test_tres():
    print("test tres")



def test_cuatro():
    print("test cuatro")