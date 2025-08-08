import allure
import pytest
import time

from allure_commons.types import AttachmentType
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


#parte de codigo para imagenes de error en allure reports
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="error", attachment_type=AttachmentType.PNG)


t=5
@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    f = Funciones_global(driver)
    f.texto_mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.texto_mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("entrando al sistema")
    yield
    print("saliendo del sistema prueba uno ok ")
    driver.close()

@pytest.fixture(scope="module")
def setup_Login_dos():
    global driver, f
    driver = webdriver.Firefox()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    f = Funciones_global(driver)
    f.texto_mixto("xpath", "//input[contains(@id,'username')]", "Admin", t)
    f.texto_mixto("xpath", "//input[contains(@id,'password')]", "admin123", t)
    f.click_mixto("xpath", "//button[contains(@id,'submit')]", t)
    print("entrando al sistema dos")
    yield
    print("saliendo del sistema prueba dos ok ")
    driver.close()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("entrando al sistema 1 ")
    f.click_mixto("xpath","//a[@href='/web/index.php/admin/viewAdminModule']",t)
    f.click_mixto("xpath","//button[contains(.,'Add')]",t)
    time.sleep(3)
    f.click_mixto("xpath","(//div[contains(@class,'oxd-select-text-input')])[1]",t)
    f.Click_XY("xpath","(//div[contains(@class,'oxd-select-text-input')])[1]",0,100,t)
    allure.attach(driver.get_screenshot_as_png(),name="Customer",attachment_type=AttachmentType.PNG)
    time.sleep(3)
    f.texto_mixto("xpath","//input[contains(@placeholder,'Type for hints...')]","test",t)
    f.click_mixto("xpath", "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[2]", t)
    f.Click_XY("xpath", "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[2]", 0, 100, t)
    f.click_mixto("xpath","//input[contains(@class,'oxd-input oxd-input--focus')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="test2", attachment_type=AttachmentType.PNG)
    driver.close()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_Login_dos")
def test_dos():
    print("entrando al sistema dos ")
    f.click_mixto("xpath","//a[@href='https://practicetestautomation.com/courses/']",3)
    allure.attach(driver.get_screenshot_as_png(), name="Customer2", attachment_type=AttachmentType.PNG)
    driver.close()



