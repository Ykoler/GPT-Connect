#web automation idea to ignore the need for an api-key
base_url = "https://chat.openai.com/"


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from credentials import email, password
import time
from random import *

timeR = lambda x :(time.sleep(x+(float(randint(0,100))/100)))


#make a simple request to the page "https://chat.openai.com/"
def setupBrowser(browser,url):
    print("Setting up browser...")
    browser.get(url)
    time.sleep(1)
    browser.get_screenshot_as_file("state0.png")
    #press the login button
    try:
        browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]').find_element(By.CSS_SELECTOR,"button").click()
    except:
        #option 2
        browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]').find_element(By.CSS_SELECTOR,"button").click()
    timeR(3)
    browser.get_screenshot_as_file("state1.png")
    #enter the email
    browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input").send_keys(email)
    #press the continue button
    browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/div[1]/div/form/div[2]/button").click()
    timeR(1)
    browser.get_screenshot_as_file("state2.png")
    #enter the password
    browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/form/div[2]/div/div[2]/div/input").send_keys(password)
    #press the login button
    browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/form/div[3]/button").click()
    timeR(1)
    browser.get_screenshot_as_file("state3.png")
    #navigae out of the first entry screen by sending a spacific siquence of keys
    ActionChains(browser).send_keys(Keys.ENTER, Keys.TAB*13, Keys.ENTER, Keys.TAB*14, Keys.ENTER).perform()
    timeR(1)
    browser.get_screenshot_as_file("state4.png")
    print("Setup complete, awaiting response...")
    timeR(1)

def reply(browser, query, response_index):
    #write the query to the input box
    browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div[2]/form/div/div[2]').find_element(By.ID,"prompt-textarea").send_keys(query)
    #press the submit button
    timeR(1)
    browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div[2]/form/div/div[2]').find_element(By.ID,"prompt-textarea").send_keys(Keys.ENTER)
    browser.get_screenshot_as_file("state5.png")
    #wait for the response to load
    timeR(5)
    browser.get_screenshot_as_file("state6.png")
    #get the response
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    response = soup.findAll("div", {"class": "flex flex-grow flex-col gap-3"})[(response_index*2)+1]
    return response.text

def conversation():
    #setup the browser
    opts = Options()
    opts.add_argument("--headless")
    browser = Chrome(options=opts)
    setupBrowser(browser,base_url)
    #start the conversation
    response_index = 0
    while True:
        query = input("You: ")
        if query == "exit":
            break
        print("AI: "+reply(browser,query,response_index))
        response_index+=1
    browser.quit()

conversation()