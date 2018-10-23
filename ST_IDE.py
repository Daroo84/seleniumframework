from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
import time


class ST_IDE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        ##self.driver = webdriver.Chrome()
        self.driver.get('https://account.smartthings.com/login/samsungaccount')
        self.driver.maximize_window()

    def testLogin(self):
        driver = self.driver
        # LOGIN IN PAGE
        email = '//*[@id="username"]'
        password = '//*[@id="password"]'
        login = '//*[@id="login-user-btn"]'
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(email))
        emailFieldElement.send_keys('srpolusa.8@gmail.com')
        passwordFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password))
        passwordFieldElement.send_keys('zaq12WSX')
        logButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login))
        logButton.click()

        time.sleep(3)  # wait 3sec and do next action

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()