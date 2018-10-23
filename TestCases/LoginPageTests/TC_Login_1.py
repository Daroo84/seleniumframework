from selenium import webdriver

import unittest
import time
import sys, os
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:/SeleniumDriver/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")


        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
