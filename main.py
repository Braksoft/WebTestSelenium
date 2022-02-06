from selenium import webdriver
import unittest


# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

class TestWebBank(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Prog\DriverSE\chromedriver.exe')
        self.base_url = 'http://automationpractice.com/index.php'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    # ---------------------------------------------------------------

    def test_summarry(self):
        driver = self.driver
        driver.get(self.base_url)


# ---------------------------------------------------------
