import time
from selenium import webdriver
from tkinter import *
import getpass
import threading
import datetime
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


writing = True
browser = webdriver.Firefox()



def logs():
   global writing
   global browser
   logs_content = browser.find_element_by_css_selector(".content")
   if writing:
       curent_time = datetime.datetime.now()
       threading.Timer(120, logs).start()
       save_path = 'C:/Users/' + getpass.getuser() + '/Desktop/Logs ' + curent_time.strftime("%d-%B-%Y") + '.txt'
       with open(save_path, "w") as logs_txt:
           logs_txt.write(logs_content.text)

def finding_errors():
    curent_time = datetime.datetime.now()
    txt_file = open('C:/Users/' + getpass.getuser() + '/Desktop/Logs ' + curent_time.strftime("%d-%B-%Y") + '.txt', 'rt')
    errors_list = []
    for line in txt_file:
        if "error" in line:
            errors_list.append(line)
        elif "warn" in line:
            errors_list.append(line)
        else:
            errors_list.append('Lack of errors and warns, be happy.')
        errors_list = '\n'.join(errors_list)
    save_path = 'C:/Users/' + getpass.getuser() + '/Desktop/errors from logs.txt'
    with open(save_path, 'w') as errors:
        errors.write(errors_list)

def hub_events():
   global browser
   temp = browser.window_handles[1]
   temp.execute_script("window.open('https://graph-na04-useast2.api.smartthings.com/hub');")
   time.sleep(7)
   #WebDriverWait(browser, 10000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table-wrap')))
   #temp = browser.find_element_by_tag_name('body')
   temp.click()
   temp.find_element_by_xpath('/html/body/main/div[2]/div[1]/table/tbody/tr[6]/td[2]/a').click()
  #select.select_by_visible_text('List Events').click()
   #browser.find_elements_by_xpath("html/body/table/tbody/tr['18']/td[2]/a").click()
   #browser.find_element_by_xpath('//tr[contains(text(),"List Events")]//a').click()


def enter_to_IDE():
   username = browser.find_element_by_id("username")
   username_input = login.get()
   username.send_keys(username_input)
   browser.find_element_by_id("next-step-btn").click()
   time.sleep(5)
   password_css = browser.find_element_by_id("password")
   password_input = password.get()
   password_css.send_keys(password_input)
   browser.find_element_by_id("login-user-btn").click()
   WebDriverWait(browser, 10000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.content')))
   logs()
   threading.Timer(10, hub_events).start()


def US_shard():
   global browser
   browser.get('https://graph-na04-useast2.api.smartthings.com/ide/logs')
   enter_to_IDE()


def EU_shard():
   global browser
   browser.get('https://graph-eu01-euwest1.api.smartthings.com/ide/logs')
   enter_to_IDE()

def kill():
   global writing
   global browser
   writing = False
   browser.quit()
   window.quit()
   window.destroy()
   finding_errors()


window = Tk()
window.title('IoT logs wypluwacz')
window['bg'] = 'steelblue1'

heading = Label(window, text = 'Export logs to txt', font = 'bold', bg = 'steelblue1')
heading.grid(row = 0, columnspan = 4)

login = StringVar()
login = Entry(window, textvariable = login)
password = StringVar()
password = Entry(window, textvariable = password)

login_heading = Label(window, text = 'Login: ',bg = 'steelblue1')
password_heading = Label(window, text = 'Password: ', bg = 'steelblue1')

menu = Menu(window)
window.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = 'Shards: ', menu = subMenu)
subMenu.add_command(label = 'US Shard', command = lambda: US_shard())
subMenu.add_command(label = 'EU Shard', command = lambda: EU_shard())


stop_button = Button(window, text = 'Kill me!', fg = 'black', padx = 20, pady = 5, command = lambda: kill())




login_heading.grid(row = 1, column = 1,padx = 30, pady = 10)
password_heading.grid(row = 2, column = 1,padx = 30, pady = 10)
login.grid(row = 1, column = 2, padx = 40, pady = 10)
password.grid(row = 2, column = 2, padx = 40, pady = 10)
stop_button.grid(row = 3, columnspan = 4)




window.mainloop()
