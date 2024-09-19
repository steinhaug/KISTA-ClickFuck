from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=selenium")  # This will use a cached session
    chrome_options.add_argument("--start-maximized")  # This will maximize the browser window
    return webdriver.Chrome(options=chrome_options)

def load_webpage(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print(f"Page loaded: {url}")

def find_element(driver, class_name):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name.lstrip('.')))
    )
    return element

def take_screenshot(driver, count):
    filename = f"cc-10-{count:02d}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")

def pronounce_biggest_answer(count):
    print(f"The biggest answer is: {count}")

def main():
    driver = setup_driver()
    
    try:
        load_webpage(driver, "https://www.instagram.com")
        
        for count in range(1, 6):
            element = find_element(driver, ".xvbhtw8.x78zum5.xdt5ytf")
            take_screenshot(driver, count)
            time.sleep(1)  # Wait a bit between actions
        
        pronounce_biggest_answer(5)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()