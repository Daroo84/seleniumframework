from selenium import webdriver
from


#--------Initialize function-------------------------------------
def DriverTestInit(self):

    self.driver = webdriver.Chrome('C:\\ChromeD\\chromedriver')



#--------Log in function----------------------------------------
def LogIn(driver):
    ##Function reads from credentials txt file login data and page address.
    if sys.platform.startswith('linux'):
        fileName=sys.path[-1]+"/WebApplication/credentials.txt"
    else:
        fileName = sys.path[-1]+"\WebApplication\credentials.txt"
    print(fileName)
    f = open(fileName)
    lines = f.readlines()
    f.close()


    #Open Login page
    driver.get(lines[0].rstrip('\n'))

    #Add Cookie
    driver.add_cookie({'name': 'loadingAnimation', 'value': 'false'})

    #Maximize window
    driver.maximize_window()

    #Login Xpaths
