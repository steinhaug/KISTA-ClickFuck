from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

varUserDataDir = "I:\\python-htdocs\\KISTA-ClickFuck\\public_html\\mySessionCache-03-fb"
varChromeService = 'G:\\chrome-webdrivers\\129-chromedriver-win64\\chromedriver.exe'

varLogItems = 'i:\\log.log'
varLogLinks = 'i:\\video.log'

def setup_driver():
    service = Service(executable_path=varChromeService)
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=selenium")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("profile-directory=Profile 1")
    chrome_options.add_argument(f"user-data-dir={varUserDataDir}")
    return webdriver.Chrome(service=service, options=chrome_options)

def load_webpage(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print(f"Page loaded: {url}")

def scroll_page(driver):
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Wait for content to load

def get_recommend_list_items(driver):
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-e2e="recommend-list-item-container"]'))
    )
    return items

def append_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def main():
    driver = setup_driver()
    
    try:
        load_webpage(driver, "https://tiktok.com")
        
        for _ in range(5):
            # Select tag "#main-content-homepage_hot"
            main_content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "main-content-homepage_hot"))
            )
            
            scroll_page(driver)
            
            items = get_recommend_list_items(driver)
            
            for item in items:
                # Append item content to i:\log.log
                append_to_file(varLogItems, item.text)
                
                # Find video element and get src
                try:
                    video = item.find_element(By.TAG_NAME, 'video')
                    video_src = video.get_attribute('src')
                    append_to_file(varLogLinks, video_src)
                except:
                    print("No video found in this item")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()