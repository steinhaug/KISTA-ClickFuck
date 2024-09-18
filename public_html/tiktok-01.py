from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

varChromeDriver = "G:\\chrome-webdrivers\\129-chromedriver-win64\\chromedriver.exe"
varChromeHeadlessShell = "G:\\chrome-webdrivers\\129-chrome-headless-shell-win64\\chrome-headless-shell.exe"
varChrome = "G:\\chrome-webdrivers\\129-chrome-win64\\chrome.exe"

varUserData = "C:\\Users\\steinhaug\\AppData\\Local\\Google\\Chrome\\User Data"
varProfile = "G:\\chrome-bank\\flipper.001"

service = Service(executable_path=varChromeDriver)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

#options.add_argument("user-data-dir=./mySessionCache")
#options.add_argument(f"user-data-dir={varUserData}")
options.add_argument("profile-directory=Profile 1")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=options)

# Here comes logic

driver.get('https://www.tiktok.com')
print("Page loaded")

link = driver.find_element(by=By.XPATH, value='//a[@target="_blank"]')
link.click()
print("Navigated to ad page")


try:
    ad = driver.find_element(By.XPATH,"//div/ad-selector")
    ad.click()
    print('Ad clicked')
except:
    print('No ad found')


attempts = 0
while attempts < 3:
    driver.refresh()
    try:
        ad = driver.find_element(By.XPATH,"//div/ad-selector")
        ad.click()
        print('Ad clicked')
        break
    except:
        print(f'Retrying... attempt {attempts + 1}')
    attempts += 1


#options.add_argument(f"user-data-dir={varUserData}")
