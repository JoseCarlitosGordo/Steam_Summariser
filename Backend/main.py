from flask import Flask, jsonify, render_template
from requests import get
from steam_web_api import Steam
app = Flask(__name__, template_folder="/templates")
KEY = "532137961076F4F8A8E5840E5C552DCA"

steam = Steam(KEY)

class Searcher:
    @app.route("/")
    @staticmethod
    def index():
        return render_template("index.html")

    @app.route("/find_game", strict_slashes=False, methods=["POST"])
    @staticmethod
    def find_game(search_parameter):
        game_list = []
        games = steam.apps.search_games(search_parameter)
        
        for game in games["apps"]:
            game_list.append(game)
        return jsonify(game_list)


    
# print(steam.users.search_user("DahoovieDoober"))
# games = steam.apps.search_games("terr")
# for game in games["apps"]:
#     print(f"{game} \n")

