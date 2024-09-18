from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

varChromeDriver = "G:\\chrome-webdrivers\\129-chromedriver-win64\\chromedriver.exe"
varChromeHeadlessShell = "G:\\chrome-webdrivers\\129-chrome-headless-shell-win64\\chrome-headless-shell.exe"
varChrome = "G:\\chrome-webdrivers\\129-chrome-win64\\chrome.exe"

service = Service(executable_path=varChromeDriver)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=options)

# G:\chrome-webdrivers\chrome-win64\chrome.exe
# G:\chrome-webdrivers\chrome-headless-shell-win64\chrome-headless-shell.exe
# G:\chrome-webdrivers\chromedriver-win64\chromedriver.exe

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

#url = "https://www.tiktok.com"
#driver.get(url)
#time.sleep(5)
#driver.quit()


try:
        # Step 2: Launch URL (TikTok as an example) and wait for it to load
        url = "https://www.tiktok.com"
        driver.get(url)
        print("Page loaded")

        # Step 3: Click a link (replace with an actual ad link selector if needed)
        try:

                wait = WebDriverWait(driver, 20)
                link= wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='userName name']"))).get_attribute("href")
                print (link)

                #link = driver.find_element_by_xpath('//a[@target="_blank"]')  # Placeholder selector
                link.click()
                time.sleep(2)  # Wait for page to load after click
                print("Navigated to ad page")
        except NoSuchElementException:
                print("No link found, skipping")

        # Step 4: Look for an ad on the page (update with the actual ad selector)
        try:
                ad = driver.find_element_by_css_selector('div.ad-selector')  # Placeholder selector
                ad.click()
                print('Ad clicked')
        except NoSuchElementException:
                print('No ad found')

except Exception as e:
        print(f"An error occurred: {e}")

finally:
        # Close the browser after the run
        driver.quit()


