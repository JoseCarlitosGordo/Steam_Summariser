import json
import requests
batch_size = 100
with open("games.json", "r") as outputJson:
    games = json.load(outputJson)

try:
    with open("current_index.json", "r") as outputJson:
        state = json.load(outputJson)
        last_index = state.get("last_index")
except:
    last_index = 0

end_index = min(last_index + 100, len(games))
gameslist = games[last_index:end_index]

for game in gameslist: 
    game_to_search = requests.get(f"https://store.steampowered.com/api/appdetails?appids={game["appid"]}")

with open("current_index.json", "r") as outputJson:
    state = json.load(outputJson)
    last_index = state.get("last_index")