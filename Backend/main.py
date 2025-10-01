from flask import Flask, request,  render_template
from DataBase import DatabaseIndex
# import requests
# import jinja2
# import json
#from steam_web_api import Steam
app = Flask(__name__, template_folder="/templates")
KEY = "532137961076F4F8A8E5840E5C552DCA"

#steam = Steam(KEY)

@app.route("/api")
def display_games():  
    pass

@app.route("/api/find_game")
def find_game():
    pass
    