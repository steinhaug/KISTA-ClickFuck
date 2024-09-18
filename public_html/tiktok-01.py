from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException
import time

service = Service(executable_path='G:\chrome-webdrivers\chromedriver-win64-dev\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("user-data-dir=./mySessionCache")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.tiktok.com')
print("Page loaded")



link = driver.find_element_by_xpath('//a[@target="_blank"]')
link.click()
print("Navigated to ad page")


try:
    ad = driver.find_element_by_css_selector('div.ad-selector')
    ad.click()
    print('Ad clicked')
except:
    print('No ad found')


attempts = 0
while attempts < 3:
    driver.refresh()
    try:
        ad = driver.find_element_by_css_selector('div.ad-selector')
        ad.click()
        print('Ad clicked')
        break
    except:
        print(f'Retrying... attempt {attempts + 1}')
    attempts += 1


options.add_argument("user-data-dir=./mySessionCache")
