import requests
from config import WEATHER_API_KEY

def get_weather(city, state):
    url = 'http://api.wunderground.com/api/{}/conditions/q/{}/{}.json'.\
        format(WEATHER_API_KEY, state, city)
    r = requests.get(url)
    return r.json()['current_observation']