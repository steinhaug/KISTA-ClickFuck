# Python program to demonstrate
# selenium

# working
# https://iqss.github.io/dss-webscrape/finding-web-elements.html

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.tiktok.com")

# get element 
element = driver.find_element(By.XPATH, "//form[input/@name ='search']")

# print complete element
print(element)