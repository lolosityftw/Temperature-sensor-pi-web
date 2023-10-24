import Adafruit_DHT
import time
from flask import Flask, render_template

sensor = Adafruit_DHT.DHT22
sensor_pin = 4
running = True
       
app = Flask(__name__)



def get_sensor():
    h, t = Adafruit_DHT.read_retry(sensor, sensor_pin)
    return round(h, 2), round(t, 2)

@app.route("/")
def index():
    h,t=get_sensor()
    return render_template("index.html", h=h, t=t)

@app.route("/json")
def json():
    h,t=get_sensor()
    return {
        "humidity": h,
        "temp": t,
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

