

#urlMeta = ["https://www.tiktok.com/search?q=welding&t=1726737305811", "main-content-general_search", "main-content-homepage_hot", '//data-e2e="search_top-item-list"']

# https://css2xpath.github.io/


urlMeta = ["https://www.instagram.com/explore/", "", "", "", "", "", ""]
urlMeta = ["https://soundcloud.com/discover", "playableTile__heading,sc-link-dark", "e19c29qe10", "", "", "", "", ""]
urlMeta = ["https://www.facebook.com/", "reg_pages_msg", "", "", ""]

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get(urlMeta[0])

main_content = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, urlMeta[1]))
)

# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("you@email.com")
password.send_keys("yourpassword")

# Step 4) Click Login
submit.click()