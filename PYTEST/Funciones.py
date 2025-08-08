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
from selenium.webdriver import ActionChains


class Funciones_global():

    def __init__(self,driver):
        self.driver = driver

    def Tiempo(self, tiem):
        t = time.sleep(tiem)
        return t

    def Navegar(self, Url,tempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("pagina abierta"+ str(Url))
        t = time.sleep(tempo)
        return t




    def texto_xpath_validar(self,xpath, texto, tiempo):
        try:
            #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("escribiendo en el campo {} el texto{} ".format(xpath,texto))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro " + xpath)




    def click_xpath_validar(self,xpath, tiempo):
        try:
            #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("damos click en el campo {} " .format(xpath))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro " + xpath)


    def Salida(self):
        print("Se termina la prueba")



    '''
    def Select_xpath_text(self,xpath,texto, tiempo):
        try:
            #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            val.select_by_visible_text(texto)
            print("El campo seleccionado es {} " .format(texto))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro " + xpath)
    '''




    def Select_xpath_type(self,xpath,type,dato, tiempo):
        try:
            #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            if (type =="texto"):
                val.select_by_visible_text(dato)
            elif(type=="index"):
                val.select_by_index(dato)
            elif(type=="value"):
                val.select_by_value(dato)

            #val.select_by_visible_+type+(dato)
            print("El campo seleccionado es {} " .format(dato))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro " + xpath)
            return t


    def Select_ID_type(self, id, type, dato, tiempo):
        try:
             # val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val = Select(val)
            if (type == "texto"):
                val.select_by_visible_text(dato)
            elif (type == "index"):
                val.select_by_index(dato)
            elif (type == "value"):
                val.select_by_value(dato)

            # val.select_by_visible_+type+(dato)
            print("El campo seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro {}"  .format(id))



    def Upload_xpath_type(self, xpath, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            time.sleep(4)

        except TimeoutException as ex:
            print(ex.msg)




    def Check_xpath_(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("El check seleccionado es {} ".format(xpath))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no se encontro " + xpath)
            return t



    def Check_xpath_multiples(self,tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("El check seleccionado es {} ".format(num))
                t = time.sleep(tiempo)
                return t

        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("elemento no se encontro " + num)


#SEX- search element xpath
    def SEX(self,elemento):
        val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self,elemento):
        val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def texto_mixto(self,type,selector, texto, tiempo):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.XPATH, selector)
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("escribiendo en el campo {} el texto{} ".format(selector,texto))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.ID, selector)
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("escribiendo en el campo {} el texto{} ".format(selector,texto))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)



    def click_mixto(self,type,selector, tiempo):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                print("Dando click en {} -->{} ".format(selector,selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print("Dando click en {} -->{} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)

    def Existe(self, type, selector, tiempo):
        if (type == "xpath"):
            try:
                # val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                print("el elemento {} --> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
                return "No Existe"
        elif (type == "id"):
            try:
                # val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print("Dando click en {} -->existe".format( selector))
                t = time.sleep(tiempo)
                return "Existe"

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
                return "No Existe"




    def double_click(self,type,selector, tiempo=3):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("doubleClick en {}". format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("doubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)


    def click_derecho(self,type,selector, tiempo=3):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.XPATH, selector)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho {}". format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.ID, selector)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click dercho {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)




    def Drag_Drop(self,type,selector,destino, tiempo=3):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.XPATH, selector)
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("drag and drop {}". format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.ID, selector)
                val = self.SEI(selector)
                val2 = self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Drag and drop {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)




    def Drag_DropXY(self,type,selector,x,y, tiempo=3):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.XPATH, selector)
                self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("drag and drop {}". format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.ID, selector)
                self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,x,y).perform()
                print("Drag and drop {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)


    def Click_XY(self,type,selector,x,y, tiempo=3):
        if(type=="xpath"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.XPATH, selector)
                #self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val,x,y).click().perform()
                print("Click al elemento {} coordenada {},{}". format(selector,x,y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)
        elif(type=="id"):
            try:
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, xpath))
                #val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                #val = self.driver.find_element(By.ID, selector)
                #self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento {} coordenada {},{}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("elemento no se encontro " + selector)





'''
    def Existe(self,tipo,selector, tiempo):
        if tipo == "xpath":
            try:
                val = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(By.XPATH, selector))
                val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
                val = self.driver.find_element(By.XPATH, selector)
                print("el elemento {}--> existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro el elemento" + selector)
                return  "No existe"
        elif tipo=="id":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By.ID, selector))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                print("el elemento {}--> existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro el elemento" + selector)
                return "No existe"

'''











'''
   def texto_ID(self,ID,texto,tiempo):
        val = self.driver.find_element(By.ID, ID)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(tiempo)
        return t
'''