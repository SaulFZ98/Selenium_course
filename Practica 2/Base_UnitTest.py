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



class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        t = 3
    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        time.sleep(2)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()








