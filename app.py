import requests
from flask import Flask, render_template, redirect, url_for
from weather import get_weather
from send_sms import send_sms
from config import INSTA_CLIENT_ID

app = Flask(__name__)


def get_photos(lat, longi):
    url = 'https://api.instagram.com/v1/media/search?lat={}&lng={}&client_id={}&count=50'
    url = url.format(lat, longi, INSTA_CLIENT_ID)
    r = requests.get(url).json()
    return r


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city/<state>/<city>')
def get_city(state, city):
    weather = get_weather(city, state)
    temperature = weather['temperature_string']
    lat = weather['display_location']['latitude']
    longi = weather['display_location']['longitude']
    photos = get_photos(lat, longi)
    return render_template('city.html', city=city.capitalize(),
                           state=state.upper(), weather=temperature,
                           photos=photos)


@app.route('/text/<state>/<city>')
def text_me(state, city):
    send_sms("You should visit {}, {}".format(city, state))
    return redirect(url_for('get_city', state=state, city=city))


if __name__=="__main__":
    app.run(port=8080, debug=True)
