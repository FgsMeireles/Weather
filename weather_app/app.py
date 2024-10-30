from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

API_KEY  = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city):
    try:
        response = request.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'pt-br'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f'Erro ao fazer sua busca: {err}')
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    data = request.get_json()
    city = data['city']
    weather_data = get_weather(city)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)