# web automation idea to ignore the need for an api-key
base_url = "https://chat.openai.com/"

import gptmanager
from imports import *
from credentials import email, password
from botdetection import *
from drivermanager import *


def reply(browser, query, response_index):
    action = ActionChains(browser)
    # write the query to the input box
    input_box = browser.find_element(
        by=By.XPATH, value='//textarea[contains(@placeholder, "Send a message")]'
    )
    for word in slice_sentence(query):
        time.sleep(0.1 + randint(0, 100) / 500)
        browser.execute_script(f"arguments[0].value = '{word}';", input_box)
        # browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div[2]/form/div/div[2]').find_element(By.ID,"prompt-textarea").send_keys(word)

    # press the submit button
    timeR(2)
    action.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()

    # browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/div[2]/form/div/div[2]').find_element(By.ID,"prompt-textarea").send_keys(Keys.ENTER)
    # wait for the response to load, we will check evety 1 seconds if the html has changed
    time.sleep(1)
    while True:
        prev_html = browser.page_source
        time.sleep(1)
        if prev_html == browser.page_source:
            break
    timeR(1, 0.1)
    # get the response
    soup = BeautifulSoup(browser.page_source, "html.parser")
    response = soup.findAll("div", {"class": "flex flex-grow flex-col gap-3"})[
        (response_index * 2) + 1
    ]
    return response.text


def conversation(delete=False):
    # setup the browser
    launch_chrome_with_remote_debugging('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"', 9222,"https://chat.openai.com/")
    browser = initialize_chrome_driver(9222)
    browser.get(base_url)

    gptmanager.setupBrowser(browser, base_url, email, password)
    action = ActionChains(browser)
    # start the conversation
    response_index = 0
    while True:
        query = input("You: ")
        if query == "exit":
            break
        if query == "clear":
            response_index = 0
            gptmanager.deleteConversation(browser)
            print("Conversation cleared")
            continue
        if query == "status":
            browser.get_screenshot_as_file("screenshot.png")
            print("Screenshot saved")
            continue
        start = time.time()
        reply = reply(browser, query, response_index)
        while reply == "":
            browser.refresh()
            reply = reply(browser, query, response_index)
        print("AI: " + reply)
        print("Time for response: " + str(time.time() - start))
        response_index += 1
    if delete:
        gptmanager.deleteConversation(browser)
    browser.quit()


conversation(delete=True)
