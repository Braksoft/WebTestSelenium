import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class smoke_test_home_page(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://automationpractice.com/index.php'
        self.driver = webdriver.Chrome(executable_path=r'C:\SE\chromedriver.exe')

    def tearDown(self):
        self.driver.quit()

    def assert_text(self, url, driver, xpath, expected_text):
        self.driver.get(url)
        find_element = driver.find_element(By.XPATH, xpath)
        actual_text = find_element.text
        self.assertEqual(actual_text, expected_text,
                         f'Expected {expected_text} differ from actual title {actual_text} on page: {url}')

    # ------ Test the item exists and is properly named -------------
    def test_contact_us(self):
        xpath = '//*[@id="contact-link"]'
        expected_text = 'Contact us'
        self.assert_text(self.base_url, self.driver, xpath, expected_text)

    def test_sign_in(self):
        xpath = '//*[@class="login"]'
        expected_text = 'Sign in'
        self.assert_text(self.base_url, self.driver, xpath, expected_text)

    # ----------- Test is element responds

    def test_button_contact_us(self):
        xpath = '//*[@id="contact-link"]'
        expected_url = "http://automationpractice.com/index.php?controller=contact"
        driver = self.driver
        driver.get(self.base_url)

        find_button_contact_us = driver.find_element(By.XPATH, xpath)
        find_button_contact_us.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, expected_url,
                         f'Actual {driver.current_url} url is inappropriate {expected_url} ')

    def test_len_product_box(self):
        expected_len = 7
        xpath = '//*[@id="homefeatured"]//*[@class="left-block"]'

        driver = self.driver
        driver.get(self.base_url)

        len_of_element = driver.find_elements(By.XPATH, xpath)

        actual_len = len(len_of_element)
        self.assertEqual(expected_len, actual_len, f'Products number differ for page {self.base_url}')
