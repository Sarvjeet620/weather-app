from flask import Flask, render_template, request
import weather  # 👈 tumhara original code
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    advice = None

    if request.method == "POST":
        city = request.form["city"]

        # Tumhara function use kar rahe hain
        data = weather.get_weather_data(city)

        if data:
            weather_main = data.get('weather', [{}])[0].get('main', '')

            result = {
                "city": city,
                "temp": data["main"]["temp"],
                "feels": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "desc": data["weather"][0]["description"]
            }

            # Tumhara advice function use
            advice = weather.get_weather_advice(weather_main)

    return render_template("index.html", result=result, advice=advice)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)