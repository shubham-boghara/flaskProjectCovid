from flask import Flask, render_template, request
import requests
import json
import re

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


class Fetch:
    def __init__(self, url, **params):
        self.ROOT = "https://cdn-api.co-vin.in/api"
        self.URL = f"{self.ROOT}{url}"
        self.PARAMS = params
        self.KEY = " "
        self.TOKEN = " "

    def __str__(self):
        return f"{self.URL}"

    def getData(self):
        res = requests.get(self.URL, params=self.PARAMS).json()
        return res

    def postData(self, **obj):
        res = requests.post(self.URL, data=json.dumps(obj)).json()
        return res


@app.route("/generateOTP")
def generateOTP():
    fetch = Fetch("/v2/auth/public/generateOTP")
    data = fetch.postData(mobile="9512793550")

    return "hello"


@app.route('/findByPin')
def findByPin():
    pincode = request.args.get("pincode")
    date = request.args.get("date")
    d1 = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
    fetch = Fetch("/v2/appointment/sessions/public/findByPin", pincode=f"{pincode}", date=f"{d1}")
    data = fetch.getData()

    return render_template("searchBypincode.html", data=data.get("sessions"), pincode=pincode, date=date)


@app.route("/calendarByPin")
def calendarByPin():
    fetch = Fetch("/v2/appointment/sessions/public/calendarByPin", pincode="395006", date="6-06-2021")
    data = fetch.getData()

    return data


@app.route('/findByDistrict')
def findByDistrict():
    fetch = Fetch("/v2/appointment/sessions/public/findByDistrict", district_id="512", date="6-06-2021")
    data = fetch.getData()

    return data


@app.route("/calendarByDistrict")
def calendarByDistrict():
    fetch = Fetch("/v2/appointment/sessions/public/calendarByDistrict", district_id="200", date="6-06-2021")
    data = fetch.getData()

    return data


@app.route('/')
def main():
    return render_template("index.html")
