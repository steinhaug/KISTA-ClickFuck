from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time
from selenium.common.exceptions import NoSuchElementException


# working

# Function to setup and run browser automation
def run_session():
    # Setting up Chrome options to use a persistent session

    service = Service(executable_path='G:\chrome-webdrivers\chromedriver-win64-dev\chromedriver.exe')
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
        driver.get('https://www.tiktok.com')
        print("Page loaded")

        # Step 3: Click a link (replace with an actual ad link selector if needed)
        try:
            link = driver.find_element_by_xpath('//a[@target="_blank"]')  # Placeholder selector
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

# Run the session
run_session()
