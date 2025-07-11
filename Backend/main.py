from flask import Flask 
from steam_web_api import Steam

KEY = "532137961076F4F8A8E5840E5C552DCA"

steam = Steam(KEY)


print(steam.users.search_user("DahoovieDoober"))
games = steam.apps.search_games("terr")
for game in games["apps"]:
    print(f"{game} \n")

