from gptconnect import GPT_Connect
from credentials import email, password

gpt = GPT_Connect()
gpt.initiate_driver(email=email, password=password, debbug=True)
gpt.conversation()