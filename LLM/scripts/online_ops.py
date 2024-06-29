import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import json
import pyautogui
import time
import keyboard as k

class OnlineOperations:
    def __init__(self):
        """Initialize any necessary variables
        """
        var_ = None

    def find_my_ip(self):
        """Returns IP address as a dictionary"""
        ip_address = requests.get('http://api64.ipify.org?format=json').json()
        return ip_address

    def search_on_wikipedia(self, query:str):
        """Searches a topic on wikipedia and returns a summary"""
        results = wikipedia.summary(query, sentences = 2)
        return results

    def play_on_youtube(self, video:str):
        """Plays a video on youtube using PyWhatKit
        Input:
            video: a topic, not a link address
        """
        kit.playonyt(video)

    def search_on_google(self, query:str):
        """Searches for a topic on google"""
        kit.search(query)

    def send_whatsapp_message(self, number:str, message:str):
        """Requires to be signed in to Whatsapp web. Sends a whatsapp message from the logged in account to the specified number
        Input:
            number: str - recipient for the message
            message: str - contents to be sent"""

        kit.sendwhatmsg_instantly(f"+{number}", message)

    def get_latest_news(self):
        NEWS_API_KEY = config("NEWSAPI")
        news_headlines = []
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
        articles = res['articles']
        for article in articles:
            news_headlines.append(article['title'])
        return news_headlines[:5]

    def get_weather_report(self, city:str):
        OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]
        return weather, f"{temperature}℃", f"{feels_like}℃"

    def get_trending_movies(self):
        TMDB_API_KEY = config("TMDB_API_KEY")
        trending_movies = []
        res = requests.get(
            f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
        results = res["results"]
        for r in results:
            trending_movies.append(r["original_title"])
        return trending_movies[:5]

    def get_random_joke(self):
        headers = {
            'Accept': 'application/json'
        }
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        return res["joke"]

def class_test(verbose=False):
    """Function to test all methods within Online Operations class. 
    Input:
        verbose: bool, whether to visualize function outputs or not
    """

    test_ = OnlineOperations()

    if verbose:
        print(test_.find_my_ip())
        print(test_.search_on_wikipedia("python programming language"))
        test_.play_on_youtube("python course")
        test_.search_on_google("python")
        
        # get contact info from contacts_json
        with open("LLM/datasets/contacts.json", 'r') as fp:
            contact_list = json.load(fp)
        test_.send_whatsapp_message(contact_list["test"]['number'], "Test message, ignore")
        [print(f"- {news}\n") for news in test_.get_latest_news()]
        print(test_.get_weather_report("Luzern"))
        [print(f"- {movie}\n") for movie in test_.get_trending_movies()]
        print(test_.get_random_joke())
        print("\n\nall functions ran successfully\n\n")
    else:
        def function_test(func):
            """tests a function with passed parameters. If it runs successfully, adds a point to the pass counter, if not,
            adds one to the fail count. Either way, adds 1 to total function counter
            Input:
                func: function to test, must be passed with its arguments
            Output:
                passcount: 1 or 0, not bool
                failcount: 1 or 0, not bool
                total: always 1
            """
            try:
                func
                return 1
            except:
                return 0

        score = {
            "score":0,
            "total":0
        }
        score["score"] += function_test(test_.find_my_ip())
        score["score"] += function_test(test_.search_on_wikipedia("python programming language"))
        score["score"] += function_test(test_.play_on_youtube("python course"))
        score["score"] += function_test(test_.search_on_google("python"))
        score["total"] += 4
        # get contact info from contacts_json
        with open("LLM/datasets/contacts.json", 'r') as fp:
            contact_list = json.load(fp)
        score["score"] += function_test(test_.send_whatsapp_message(contact_list["test"]['number'], "Test message, ignore"))
        score["score"] += function_test(test_.get_latest_news())
        score["score"] += function_test(test_.get_weather_report("Luzern"))
        score["score"] += function_test(test_.get_trending_movies())
        score["score"] += function_test(test_.get_random_joke())
        score["total"] += 5
        print(f"""Final Results:\n{score["score"]} functions ran successfully\n
        {score["total"] - score["score"]} functions did not run successsfully\n
        {score["total"]} total functions\n
        Score: {round(score["score"]/score["total"],2)*100}%""")
if __name__ == "__main__":
    class_test()