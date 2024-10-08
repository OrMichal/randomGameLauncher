import os
import platform
import subprocess
import random
import vdf
from random import randint

def getInstalledGames(steamPath):

    libraryFoldersPath = os.path.join(steamPath, "steamapps", "libraryfolders.vdf")
    
    with open(libraryFoldersPath, "r", encoding="utf-8") as f:
        libraries = vdf.load(f)

    games = []

    for library in libraries["libraryfolders"].values():
        steamappsPath = os.path.join(library["path"], "steamapps")
        for item in os.listdir(steamappsPath):
            if item.endswith(".acf"):

                with open(os.path.join(steamappsPath, item), "r", encoding="utf-8") as f:
                    gameInfo = vdf.load(f)
                    games.append(gameInfo["AppState"]["appid"])
    
    return games

def launchRandomGame(games):
    randomGameId = random.choice(games)
    subprocess.run(["steam", f"steam://run/{randomGameId}"])


steamPath = "zde vlož cestu k share/steam"

games = getInstalledGames(steamPath)
if games:
    launchRandomGame(games)
else:
    print("Nebyly nalezeny žádné nainstalované hry.")
