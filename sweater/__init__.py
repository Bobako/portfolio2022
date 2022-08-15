from flask import Flask

import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

app.secret_key = config["SITE"]["secret_key"]

import sweater.routes
