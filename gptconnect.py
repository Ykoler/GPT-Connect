# web automation idea to ignore the need for an api-key

from typing import Any
import gpt_manager
from imports import *
from bot_detection import *
from driver_manager import *
from messege_addons import *


class GPTConnect:
    # constructor
    def __init__(self, email, password, debug=False, hidden=True):
        if debug:
            startTime = time.time()
        self.browser = initialize_chrome_driver(debug=debug, headless=hidden)
        self.debug = debug
        gpt_manager.setupBrowser(
            self.browser,
            "https://chat.openai.com/auth/login",
            email,
            password,
            debug=debug,
            headless=hidden,
        )
        if debug:
            print("Time to initiate driver: " + str(time.time() - startTime))

    def __call__(self, query, links=[]):
        return self.reply(query, links)

    def reply(self, query, links=[]):
        start_time = time.time()
        if(len(links) > 0):
            link_addons = ["\n\n Use the transcript below to help you with your response: \n\n" + add_youtube_transcript(link) for link in links]
            query += "\n\n" + "\n\n".join(link_addons)

        #if len(query.split() > 3000):
            #raise Exception("The query(including links) must be less than 3000 words")
        # write the query to the input box
        input_box = self.browser.find_element(
            by=By.XPATH, value='//textarea[contains(@placeholder, "Send a message")]'
        )
        fast_mode = len(query.split()) > 1000

        for sentence in query.split("\n"):
            if fast_mode:
                input_box.send_keys(sentence)
            else:
                for word in slice_sentence(sentence):
                    time.sleep(0.02 + randint(0, 100) / 3000)
                    input_box.send_keys(word)
            # go down a line using shift + enter
            input_box.send_keys(Keys.SHIFT + Keys.RETURN)

        # press the submit button
        timeR(0.5, 0.5)
        input_box.send_keys(Keys.RETURN)
        if self.debug:
            print("Query sent")

        # wait for the response to load, we will check evety 1 seconds if the html has changed
        time.sleep(1)
        while True:
            prev_html = self.browser.page_source
            time.sleep(2)
            if prev_html == self.browser.page_source:
                break
        # get the response
        try:
            response = self.get_response()
        except:
            raise Exception("There was an error with the response, please try again")
        if self.debug:
            print("Time for response: " + str(time.time() - start_time))
        return response

    def status(self, filename="screenshot.png"):
        self.browser.get_screenshot_as_file(filename)

    def clear(self):
        gpt_manager.deleteConversation(self.browser)

    def clear_all(self):
        gpt_manager.deleteAllConversations(self.browser)

    def refresh(self):
        self.browser.refresh()

    def close(self):
        self.browser.quit()
    
    def __del__(self):
        self.close()

    def get_response(self, index=0):
        responses = BeautifulSoup(self.browser.page_source, "html.parser").findAll(
            "div", {"class": "flex flex-grow flex-col gap-3 max-w-full"}
        )
        return responses[2 * (index - 1) + 1].text

    def get_responses(self):
        responses = BeautifulSoup(self.browser.page_source, "html.parser").findAll(
            "div", {"class": "flex flex-grow flex-col gap-3 max-w-full"}
        )
        return responses[1::2]
    
    def get_prompt(self, index=0):
        responses = BeautifulSoup(self.browser.page_source, "html.parser").findAll(
            "div", {"class": "flex flex-grow flex-col gap-3"}
        )
        return responses[2 * (index - 1)].text


    def conversation(self, delete=False):
        # start the conversation
        print(
            """Type "exit" to exit the conversation, "clear" to clear the conversation, "status" to save a screenshot of the conversation
              otherwise type your message and press enter.
              Note: This isn't the intended way to use this library, it is just a demo of the functionality.
        """
        )
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
        if delete:
            gpt_manager.deleteConversation(self.browser)
        try:
            self.browser.close()
        except:
            pass
