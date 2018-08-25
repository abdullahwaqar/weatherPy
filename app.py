import requests
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=c4c982214c850a7ffeb1628d6a977946'

    r = requests.get(url).json()

    weather = {
        'city': 'UK',
        'temprature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'date_time': datetime.datetime.now(),
    }
    print(weather)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)