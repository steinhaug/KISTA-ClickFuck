from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

varChromeDriver = "G:\\chrome-webdrivers\\129-chromedriver-win64\\chromedriver.exe"
varChromeHeadlessShell = "G:\\chrome-webdrivers\\129-chrome-headless-shell-win64\\chrome-headless-shell.exe"
varChrome = "G:\\chrome-webdrivers\\129-chrome-win64\\chrome.exe"

# working

url1 = "https://www.tiktok.com/search?q=welding&t=1726737305811"
url2 = 'https://www.tiktok.com'

htmlId1 = "main-content-general_search"
htmlId2 = "main-content-general_search"


# Function to setup and run browser automation
def run_session():
    # Setting up Chrome options to use a persistent session

    service = Service(executable_path=varChromeDriver)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=service, options=options)

    # I:\python-htdocs\KISTA-ClickFuck\sessions
    # G:\chrome-webdrivers\chromedriver-win64-canary\chromedriver.exe
    # G:\chrome-webdrivers\chrome-win64-dev\chrome.exe
    # G:\chrome-webdrivers\chromedriver-win64-dev\chromedriver.exe

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        # Step 2: Launch URL (TikTok as an example) and wait for it to load
        driver.get(url1)
        print("Page loaded...")

        # Step 3: Click a link (replace with an actual ad link selector if needed)
        try:

            # https://selenium-python.readthedocs.io/waits.html
            element = WebDriverWait(driver, 10).until(
                #EC.presence_of_element_located((By.ID, htmlId1))
                EC.presence_of_element_located((By.ID, htmlId1))
            )
            print("Page loaded... Check.")

            link = driver.find_element(by=By.XPATH, value='//data-e2e="search_top-item-list"') #//a[@target="_blank"]
            link.click()
            time.sleep(2)  # Wait for page to load after click
            print("Navigated to ad page")
        except NoSuchElementException:
            print("No link found, skipping")

        # Step 4: Look for an ad on the page (update with the actual ad selector)
        try:

            #'data-e2e="search-card-user-link"'
            #'//data-e2e="search-card-like-container"'

            ad = driver.find_element(By.XPATH, '//data-e2e="search-card-user-link"')
            ad.click()
            print('Ad clicked')
        except NoSuchElementException:
            print('No ad found')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after the run
        driver.quit()

time.sleep(5)  

# Run the session
run_session()
