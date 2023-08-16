A python project to automate ChatGPT usage without the need for the API, using Selenium for web automation.

This project uses Selenium and Undetected-Chromedriver to automate the process of logging in and sending prompts to the AI, and then returning the response.
It isn't meant to be used as a replacement for the API, for 4 main reasons:
1. It is much slower than the API.(takes 15 seconds to login and depending on the length of the prompt, it can take some time)
2. It is not as reliable as the API, if the website changes, the project will break.(although it is easy to fix)
3. It has the limits of the website.(Hourly limit, length limit, etc.)
4. It lacks the features of the API.(such as the ability to specify the temperature, top_p, etc.)


## Installation
### Step 1: Download a ChromeDriver
Download a ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and unzip it.

### Step 2: Install the required packages
```bash
pip install -r requirements.txt
```

### Step 3: Download the project from GitHub and place all the files in a single folder.


## Usage
```python
from gptconnect import GPTConnect
gpt = GPTConnect(email="your_email", password="your_password")
#it is preferable to use an environment variable/other method to store your email and password
response = gpt.reply("What is the capital of France")
# response = "The capital of France is Paris."
```

## Documentation
### GPTConnect
#### Parameters
- `email` (str): Your email address.
- `password` (str): Your password.
- `debug` (bool): Whether to print debug messages or not. (default is False)
- `hidden` (bool): Whether to hide the browser window or not. (default is True)
#### Methods
- `reply(prompt)`: Sends a prompt to the AI and returns the response.
- `close()`: Closes the instance of the browser.
- `get_response(response_index)`: Returns the response at the specified index. (default is the last response)
- `get_responses()`: Returns a list of all the responses.
- `get_prompt(prompt_index)`: Returns the prompt at the specified index. (default is the last prompt)
- `refresh()`: Refreshes the page.
- `clear()`: Deletes the last conversation.
- `clear_all()`: Deletes all the conversations.
- `status(file_name)`: Saves a screenshot of the page to the specified file name. (default is "screenshot.png")
- `conversation(Delete)`: Initiates a conversation with the AI, if Delete is True, it will delete the conversation after it is done. (default is False)
note: The conversation method is not recommended to be used, and is mainly for testing and demonstration purposes.
