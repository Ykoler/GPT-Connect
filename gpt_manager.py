from imports import *
from bot_detection import timeR, move_mouse


def waitForLoad(browser, additional_wait_time, debug=False):
    if debug:
        print("Waiting for page to load...")
    while browser.execute_script("return document.readyState;").lower() != "complete":
        time.sleep(0.2)
        print("Waiting for page to load...")
    if debug:
        print("Page loaded")
    timeR(additional_wait_time)


def setupBrowser(browser, url, email, password, debug=False, headless=False):
    if debug:
        print("Setting up browser...")

    browser.get(url)
    waitForLoad(browser, 0.8, debug)
    action = ActionChains(browser)

    # press the login button
    action.send_keys(Keys.TAB, Keys.ENTER).perform()
    timeR(1.5)
    # enter the email
    action.send_keys(email).perform()
    if debug:
        print("Email entered")
    # press the continue button
    timeR(0.2, 0.2)
    action.send_keys(Keys.ENTER).perform()
    timeR(0.3)
    # enter the password
    browser.find_element(
        By.XPATH,
        "/html/body/div[1]/main/section/div/div/div/form/div[2]/div/div[2]/div/input",
    ).send_keys(password)
    if debug:
        print("Password entered")
    # press the login button
    action.send_keys(Keys.ENTER).perform()
    waitForLoad(browser, 1, debug)
    if debug:
        print("Login complete")
    # navigae out of the first entry screen by sending a spacific siquence of keys
    action.send_keys(
        Keys.ENTER*2
    ).perform()
    timeR(0.1, 0.2)
    if debug:
        print("Setup complete, awaiting response...")


def deleteConversation(browser):
    # will navigate to the first conversation and delete it
    # press the conversation button
    try:
        base_path = '//*[@id="__next"]/div[1]/div[1]/div/div/div/nav/div[3]/div/div/span[1]/div/ol/li[1]'
        browser.find_element(By.XPATH, base_path).click()
        timeR(0.4)
        browser.find_element(By.XPATH, base_path + "/a/div[2]/button[2]").click()
        timeR(0.4)
        ActionChains(browser).send_keys(Keys.ENTER).perform()
    except Exception:
        print("No conversations to delete")
        return False

    return True


def delete_all_chats(browser):
    # will delete all conversations
    print("Deleting all conversations...")
    while deleteConversation(browser):
        timeR(1, 0.3)
    browser.refresh()
    print("All conversations deleted")
