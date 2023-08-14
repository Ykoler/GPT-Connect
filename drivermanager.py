from imports import *

def initialize_chrome_driver(port):
    chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
    browser = webdriver.Chrome(options=chrome_options
    )
    browser.delete_all_cookies()
    browser.remove_all_credentials()
    return browser

def launch_chrome_with_remote_debugging(chrome_path, port, url):
    def open_chrome():
        chrome_cmd = f"{chrome_path} --remote-debugging-port={port} --user-data-dir=remote-profile {url}"
        os.system(chrome_cmd)

    chrome_thread = threading.Thread(target=open_chrome)
    chrome_thread.start()


