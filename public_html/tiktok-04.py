from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

varChromeService = 'G:\\chrome-webdrivers\\129-chromedriver-win64\\chromedriver.exe'
varUserDataDir = "I:\\python-htdocs\\KISTA-ClickFuck\\public_html\\mySessionCache-04"
varHTMLlog = "I:/python-htdocs/KISTA-ClickFuck/public_html/html-log.txt"

#urlMeta = ["https://www.tiktok.com", "main-content-homepage_hot", '[data-e2e="recommend-list-item-container"]']
urlMeta = ["https://www.tiktok.com/search?q=welding&t=1726737305811", "main-content-general_search", "main-content-homepage_hot", '//data-e2e="search_top-item-list"']

def setup_driver():
    service = Service(executable_path=varChromeService)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument(f"user-data-dir={varUserDataDir}")
    return webdriver.Chrome(service=service, options=chrome_options)

def scroll_and_capture(driver, scroll_count):
    main_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, urlMeta[1]))
    )

    for i in range(scroll_count):
        # Scroll down
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", main_content)
        
        # Wait for new content to load
        time.sleep(5)
        
        # Take screenshot
        timestamp = int(time.time())
        driver.save_screenshot(f"screens/ss-{timestamp}-{i+1}.png")
        
        # Extract and save HTML
        items = driver.find_elements(By.CSS_SELECTOR, urlMeta[2])
        html_content = "\n".join([item.get_attribute('outerHTML') for item in items])
        
        with open(varHTMLlog, "a", encoding="utf-8") as f:
            f.write(f"\n--- Scroll {i+1} ---\n")
            f.write(html_content)

def main():
    driver = setup_driver()
    try:
        driver.get(urlMeta[0])
        scroll_and_capture(driver, 3)  # Scroll and capture 3 times
    finally:
        driver.quit()

if __name__ == "__main__":
    main()