import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from fake_useragent import UserAgent

options = uc.ChromeOptions()
options.headless = True
options.add_argument( '--headless' )
chrome = uc.Chrome( options = options )
chrome.get("https://google.com")
time.sleep(10)
