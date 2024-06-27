import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    """Returns IP address as a dictionary"""
    ip_address = requests.get('http://api64.ipify.org?format=json').json()
    return ip_address

def search_on_wikipedia(query):
    """Searches a topic on wikipedia and returns a summary"""
    results = wikipedia.summary(query, sentences = 2)
    return results

def play_on_youtube(video):
    """Plays a video on youtube using PyWhatKit
    Input:
        video: a topic, not a link address
    """
    kit.playonyt(video)

def search_on_google(query):
    """Searches for a topic on google"""
    kit.search(query)

def send_whatsapp_message(number, message):
    """Requires to be signed in to Whatsapp web. Sends a whatsapp message from the logged in account to the specified number
    Input:
        number: str - recipient for the message
        message: str - contents to be sent"""
    import pyautogui
    import time
    import keyboard as k

    kit.sendwhatmsg_instantly(f"+{number}", message)

def send_email(receiver_address, subject, message):
    EMAIL = config("EMAIL")
    PASSWORD = ("PASSWORD")
    email = 
    



if __name__ == "__main__":
    print(find_my_ip())
    print(search_on_wikipedia("python programming language"))
    play_on_youtube("python course")
    search_on_google("python")
    send_whatsapp_message("18096133332", "No le haga caso a ete mensaje, toy testing el AI assistant que toy armando en python, ete mensaje lo mando they/them")