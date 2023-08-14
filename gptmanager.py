from imports import *
from botdetection import timeR, move_mouse

def setupBrowser(browser,url,email,password):
    print("Setting up browser...")
    browser.get(url)
    time.sleep(2)
    action = ActionChains(browser)
    
    #press the login button
    '''
    try:
        browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]').find_element(By.CSS_SELECTOR,"button").click()
    except:
        #option 2
        browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[4]').find_element(By.CSS_SELECTOR,"button").click()
    '''
    action.send_keys(Keys.TAB, Keys.ENTER).perform()
    timeR(3)
    #enter the email
    #browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input").send_keys(email)
    for i in email:
        action.send_keys(i).perform()
        timeR(0.1,0.1)
        
    print("Email entered")
    #press the continue button
    timeR(0.5)
    action.send_keys(Keys.ENTER).perform()
    timeR(1)
    #enter the password
    browser.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/div/form/div[2]/div/div[2]/div/input").send_keys(password)
    print("Password entered")
    #press the login button
    timeR(0.5)
    action.send_keys(Keys.ENTER).perform()
    timeR(1)
    print("Login complete")
    #navigae out of the first entry screen by sending a spacific siquence of keys
    action.send_keys(Keys.ENTER, Keys.TAB*13, Keys.ENTER, Keys.TAB*14, Keys.ENTER).perform()
    timeR(1)
    print("Setup complete, awaiting response...")
    timeR(1)


def deleteConversation(browser):
    #will navigate to the first conversation and delete it
    #press the conversation button
    try:
        base_path = '//*[@id="__next"]/div[1]/div[1]/div/div/div/nav/div[3]/div/div/span[1]/div/ol/li[1]'
        browser.find_element(By.XPATH, base_path).click()
        timeR(0.4)
        browser.find_element(By.XPATH,base_path + '/a/div[2]/button[2]').click()
        timeR(0.4)
        ActionChains(browser).send_keys(Keys.ENTER).perform()
    except(Exception):
        print("No conversations to delete")
        return False
    
    return True