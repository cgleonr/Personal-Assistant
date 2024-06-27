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

def get_latest_news():
    NEWS_API_KEY = config("NEWSAPI")
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res['articles']
    for article in articles:
        news_headlines.append(article['title'])
    return news_headlines[:5]




def get_weather_report(city):
    OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_trending_movies():
    TMDB_API_KEY = config("TMDB_API_KEY")
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


if __name__ == "__main__":
    print(find_my_ip())
    print(search_on_wikipedia("python programming language"))
    play_on_youtube("python course")
    search_on_google("python")
    send_whatsapp_message("18096133332", "No le haga caso a ete mensaje, toy testing el AI assistant que toy armando en python, ete mensaje lo mando they/them")
    [print(f"- {news}\n") for news in get_latest_news()]
    print(get_weather_report("Luzern"))
    [print(f"- {movie}\n") for movie in get_trending_movies()]
    print(get_random_joke())