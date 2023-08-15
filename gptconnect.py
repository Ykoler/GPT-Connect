# web automation idea to ignore the need for an api-key

import gptmanager
from imports import *
from credentials import email, password
from botdetection import *
from drivermanager import *

class GPT_Connect:
    def initiate_driver(self,email,password, debbug=False, hidden=True):
        #if(debbug):
        startTime = time.time()
        self.browser = initialize_chrome_driver(debbug=debbug)
        
        gptmanager.setupBrowser(self.browser, "https://chat.openai.com/auth/login", email, password, debbug = debbug, headless = hidden)
        self.response_index = 0
        self.action = ActionChains(self.browser)
        #if(debbug):
        print("Time to initiate driver: " + str(time.time() - startTime))


    def reply(self, query):
        # write the query to the input box
        input_box = self.browser.find_element(
            by=By.XPATH, value='//textarea[contains(@placeholder, "Send a message")]'
        )
        for word in slice_sentence(query):
            time.sleep(0.02 + randint(0, 100) / 3000)
            #self.browser.find_element(By.TAG_NAME, "textarea").send_keys(word)
            input_box.send_keys(word)

        # press the submit button
        timeR(0.5,0.5)
        #self.browser.find_element(By.TAG_NAME, "textarea").send_keys(Keys.RETURN)
        input_box.send_keys(Keys.RETURN)
        
        # wait for the response to load, we will check evety 1 seconds if the html has changed
        time.sleep(1)
        while True:
            prev_html = self.browser.page_source
            time.sleep(1)
            if prev_html == self.browser.page_source:
                break
        # get the response
        try:
            response = self.driver.find_elements(By.TAG_NAME, 'p').text
        except:
            raise Exception("There was an error with the response, please try again")
        return response
    
    def status(self, filename="screenshot.png"):
        self.browser.get_screenshot_as_file(filename)

    def clear(self):
        self.response_index = 0
        gptmanager.deleteConversation(self.browser)

    def conversation(self, delete=False):
        # start the conversation
        print('''Type "exit" to exit the conversation, "clear" to clear the conversation, "status" to save a screenshot of the conversation
              otherwise type your message and press enter.
              Note: This isn't the intended way to use this library, it is just a demo of the functionality.
        ''')
        while True:
            query = input("You: ")
            if query == "exit":
                break
            if query == "clear":
                self.clear()
                print("Conversation cleared")
                continue
            if query == "status":
                self.status()
                print("Screenshot saved")
                continue
            start = time.time()
            response = self.reply(query)
            print("AI: " + response)
            print("Time for response: " + str(time.time() - start))
            self.response_index += 1
        if delete:
            gptmanager.deleteConversation(self.browser)
        try:
            self.browser.close()
        except:
            pass
