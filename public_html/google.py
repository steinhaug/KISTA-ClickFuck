from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("G:\chrome-webdrivers\chromedriver-win64\chromedriver.exe")
import time
 
URL = "https://sites.google.com/site/ActiveRumblers/deck"
driver.get(URL)
 
#ensure page is loaded
time.sleep(3)
 
#login form is 4 iframes deep
driver.switch_to_frame(0)
driver.switch_to_frame(0)
driver.switch_to_frame(0)
driver.switch_to_frame(0)
 
#got xpath using google chrome, inspect, copy xpath
driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[2]/td[1]/div/input[3]').click()
driver.switch_to_default_content() 
 
time.sleep(2)
print ("done")