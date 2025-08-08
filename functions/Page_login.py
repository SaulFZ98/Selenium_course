import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from functions.Funciones import  Funciones_global
t=3

class Pagina_login():

    def __init__(self,driver):
        self.driver = driver

    def Login_master(self,url,name,clave,t):
        driver = self.driver
        f = Funciones_global(driver)
        f.Navegar(url, t)
        f.texto_xpath_validar("//input[contains(@id,'user-name')]", name, t)
        f.texto_xpath_validar("//input[contains(@id,'password')]", clave, t)
        f.click_xpath_validar("//input[contains(@id,'login-button')]", t)