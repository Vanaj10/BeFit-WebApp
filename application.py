import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session


from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bmr", methods = ["GET","POST"])
def bmr():
    if request.method == "POST":
        gender = request.form.get("gender").lower()
        age = int(request.form.get("age"))
        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))

        if gender == "male":
            bmr = (10*weight) + (6.25*height) - (5*age) + 5
        else:
            bmr = (10*weight) + (6.25*height) - (5*age) + 161


        return render_template("bmrtable.html",bmr=bmr)

    else:
         return render_template("bmr.html")

@app.route("/bmi", methods = ["GET" , "POST"])
def bmi():
    if request.method == "POST":
        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))
        bmi = (weight/(height * height))*10000

        return render_template("bmitable.html",bmi=bmi)

    else:
         return render_template("bmi.html")

@app.route("/fat", methods = ["GET" , "POST"])
def fat():
    if request.method == "POST":
        gender = request.form.get("gender").lower()
        age = int(request.form.get("age"))
        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))

        bmi = (weight/(height * height))*10000

        if gender == "male":
            fat = (1.2*bmi) + (0.23*age) - 16.2
        else:
            fat = (1.2*bmi) + (0.23*age) - 5.4

        return render_template("fattable.html",fat=fat)

    else:
         return render_template("fat.html")

@app.route("/weight", methods = ["GET" , "POST"])
def ideal():
    if request.method == "POST":
        gender = request.form.get("gender").lower()
        age = int(request.form.get("age"))
        height = int(request.form.get("height"))


        if gender == "male":
            if ( height >= 137 and height <= 145 ):
                MaxW = 44
                MinW = 35
            elif ( height >= 146 and height <= 155 ):
                MaxW = 55
                MinW = 38
            elif ( height >= 156 and height <= 165 ):
                MaxW = 68
                MinW = 47
            elif ( height >= 166 and height <= 175 ):
                MaxW = 80
                MinW = 50
            elif ( height >= 176 and height <= 185 ):
                MaxW = 91
                MinW = 72
            elif ( height >= 186 and height <= 195 ):
                MaxW = 103
                MinW = 81
            elif ( height >= 196 and height <= 205 ):
                MaxW = 113
                MinW = 94
            elif ( height >= 206 and height <= 213 ):
                MaxW = 124
                MinW = 108
        else:
            if ( height >= 137 and height <= 145 ):
                MaxW = 42
                MinW = 35
            elif ( height >= 146 and height <= 155 ):
                MaxW = 52
                MinW = 40
            elif ( height >= 156 and height <= 165 ):
                MaxW = 62
                MinW = 46
            elif ( height >= 166 and height <= 175 ):
                MaxW = 72
                MinW = 54
            elif ( height >= 176 and height <= 185 ):
                MaxW = 82
                MinW = 65
            elif ( height >= 186 and height <= 195 ):
                MaxW = 92
                MinW = 73
            elif ( height >= 196 and height <= 205 ):
                MaxW = 102
                MinW = 84
            elif ( height >= 206 and height <= 213 ):
                MaxW = 109
                MinW = 96

        return render_template("weighttable.html",MaxW=MaxW, MinW=MinW)

    else:
         return render_template("weight.html")


