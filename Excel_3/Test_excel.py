
import time
import unittest

from Funciones_ex import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from functions.Funciones import Funciones_global


tg=2

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome()


    def test1(self):
        driver = self.driver
        f = Funciones_global(driver)
        fe = Fun_excel(driver)
        f.Navegar("https://demoqa.com/text-box#google_vignette",tg)
        ruta = "C://Users//saul.frias//PycharmProjects//SeleniumProject//Excel//Datos.xlsx"
        filas = fe.getRowCount(ruta,"Sheet1")

        for r in range(2,filas+1):
            nombre = fe.readData(ruta,"Sheet1",r,1)
            email = fe.readData(ruta,"Sheet1",r,2)
            dir1 = fe.readData(ruta,"Sheet1",r,3)
            dir2 = fe.readData(ruta,"Sheet1",r,4)

            f.texto_mixto("id","userName",nombre,tg)
            f.texto_mixto("id", "userEmail", email, tg)
            f.texto_mixto("id", "currentAddress", dir1, tg)
            f.texto_mixto("id", "permanentAddress", dir2, tg)
            f.click_mixto("id", "submit", tg)

            e = f.Existe("id","name",tg)
            if e=="Existe":
                print("El elemento se inserto correctamente")
                fe.writeData(ruta,"Sheet1",r,5,"insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta,"Sheet1",r,5,"Error")
