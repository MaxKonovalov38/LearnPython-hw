from flask import Flask
from weather import weather_by_city
app = Flask(__name__)

@app.route("/")
def index():
    weather = weather_by_city("Irkutsk,Russia")
    if weather:
        return f"Сейчас в Иркутске {weather['temp_C']} град., ощущается как {weather['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен."

if __name__ == "__main__":
    app.run(debug=True)