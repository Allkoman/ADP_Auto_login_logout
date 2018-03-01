from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
baseurl = "https://my.adp.com/static/redbox/login.html"
username = "USERNAME"
password = "PASSWORD"

xpaths = { 'usernameTxtBox' : "//input[@name='user']",
           'passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//*[@id='login']/div",
          'dashbboard': "//*[@id='framework-container']/div[1]/ul/li[2]/a",
          'signout' : "/html/body/div/div/div[7]/div[2]/div[2]/div/div/div/div/div[4]/div[2]/div/div/div/div/div/time-punch-tile/div/div/div/div[2]/button"
         }
driver1 = webdriver.Firefox(executable_path=r'WEBDRIVER PATH')
driver1.get(baseurl)
driver1.maximize_window()
driver1.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
driver1.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
driver1.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
driver1.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
driver1.find_element_by_xpath(xpaths['submitButton']).click()
time.sleep(10)
driver1.find_element_by_xpath(xpaths['dashbboard']).click()
time.sleep(10)
driver1.find_element_by_xpath(xpaths['signout']).click()
driver1.close()
time.sleep(1800)
driver1 = webdriver.Firefox(executable_path=r'WEBDRIVER PATH')
driver1.get(baseurl)
driver1.maximize_window()
driver1.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
driver1.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
driver1.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
driver1.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
driver1.find_element_by_xpath(xpaths['submitButton']).click()
time.sleep(10)
driver1.find_element_by_xpath(xpaths['dashbboard']).click()
time.sleep(10)
driver1.find_element_by_xpath(xpaths['signout']).click()
driver1.close()
