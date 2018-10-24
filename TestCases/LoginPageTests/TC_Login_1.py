from selenium import webdriver

import unittest
import time
import sys
import os
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox(executable_path="C:/SeleniumDriver/geckodriver.exe")
        # cls.driver = webdriver.Chrome(executable_path="C:/SeleniumDriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(3)

    def test_02_login_invalid_username(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()

        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials12")



        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        # cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/d.staron/PycharmProjects/untitled/Drivers/Reports'))
