from flask import Flask, request,  render_template
from DataBase import DatabaseIndex
import requests
import jinja2
import json
#from steam_web_api import Steam
app = Flask(__name__, template_folder="/templates")
KEY = "532137961076F4F8A8E5840E5C552DCA"

#steam = Steam(KEY)

class Searcher:
    def __init__(self):
        self.__database = DatabaseIndex("SteamDatabase.db")
        self.__empty_database = False
    @app.route("/")
    @staticmethod
    def index(self):
        if (self.__empty_database is False):
            response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
            games = response.json()["applist"]["apps"] #appid, gameName
            # for game in games:
            #     query = "INSERT INTO "
            
        
        else:
            pass
        return render_template("index.html")

    @app.route("/find_game", strict_slashes=False, methods=["POST"])
    @staticmethod
    def find_game(self):
        pass
        # search_parameter = request.form.get("game_name")
        # game_list = []
        # response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
        # games = response.json()["applist"]["apps"] #appid, gameName
        # for game in games:
        #     pass
        
        # for game in games["apps"]:
        #     game_list.append(game)
        # return render_template("index.html", result = game_list)


    
# print(steam.users.search_user("DahoovieDoober"))
# games = steam.apps.search_games("call")
# for game in games["apps"]:
#     print(f"{game} \n")

