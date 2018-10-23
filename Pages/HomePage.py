
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logut_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logut_link_linkText).click()
