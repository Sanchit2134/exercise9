#Akhbar padkhe sunaoo
import json
import requests
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak("Todays news is ")
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=320fda6f627349b5bd577d2e0f19e1a1'
    news = requests.get(url).text
    news_dict = json.loads(news)
    art = news_dict['articles']
    for i in art:
        speak(i['title'])
        print(i['title'])
        speak("Next news")
speak("Thanks for listening")
