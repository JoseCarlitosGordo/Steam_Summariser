import json
import requests
import sqlite3
import time
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

for game in gameslist:
    connection_obj = sqlite3.connect("games.db")
    cursor_obj = connection_obj.cursor()
    id = game["appid"]
    game_to_search = requests.get(f"https://store.steampowered.com/api/appdetails?appids={id}")
    game_found = game_to_search.json()
    type = game_found[id]["data"]["type"]
    game_name = game_found[id]["data"]["name"]
    image_link = game_found[id]["data"]["header_image"]
    detailed_descrip = game_found[id]["data"]["detailed_description"]
    
    cursor_obj.execute("INSERT INTO Games VALUES (?, ?, ?, ?, ?)", (id, type, game_name, image_link, detailed_descrip))
    connection_obj.commit()
    connection_obj.close()
    time.sleep(0.5)

#TODO: Update this to store end_index. Also correctly format game_to_search so that it adds the result to db

#stores end index, which becomes the next current_index
with open("current_index.json", "w") as outputJson:
    stored_index = json.dump(end_index, outputJson)



