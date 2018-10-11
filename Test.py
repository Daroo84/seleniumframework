import unittest

from selenium import webdriver

driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path="C:\\SeleniumDriver\\geckodriver.exe")
#self.browser = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()

if __name__ == '__main__':

    unittest.main()
