import json
import requests
import sqlite3
import time
from DataBase import database
batch_size = 100
with open("games.json", "r") as outputJson:
    games = json.load(outputJson)

try:
    with open("current_index.json", "r") as outputJson:
        state = json.load(outputJson)
        last_index = state.get("last_index")
        if last_index == len(games):
            #raise error, which resets the last_index back to zero. good for keeping the db up to date
            raise ValueError()
except:
    last_index = 0

end_index = min(last_index + 100, len(games))
gameslist = games[last_index:end_index]

database.reopen_connection()
for game in gameslist:
    try:
       
        id = game["appid"]
        game_to_search = requests.get(f"https://store.steampowered.com/api/appdetails?appids={id}")
        game_found = game_to_search.json()
        type = game_found[str(id)]["data"]["type"]
        game_name = game_found[str(id)]["data"]["name"]
        image_link = game_found[str(id)]["data"]["header_image"]
        detailed_descrip = game_found[str(id)]["data"]["detailed_description"]
        
        database.add_new_game(id, type, game_name, image_link, detailed_descrip)
        time.sleep(0.5)
    #in the cases where nothing is found, print the key that it tries to access instead
    except KeyError as e:
        print(e)

database.close_connection()

#stores end index, which becomes the next current_index
with open("current_index.json", "w") as outputJson:
    json.dump(end_index, outputJson)



