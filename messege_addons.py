#a file to allow the bot to add files and links to the message
from imports import *

def add_youtube_transcript(url, language='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(url.split('v=')[1], languages=[language])
    except:
        return None
    text = ''
    for line in transcript:
        text += line['text'] + ' '
    return text
