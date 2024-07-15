import os
import platform
import subprocess
import random
import vdf
from random import randint

def get_installed_games(steam_path):

    library_folders_path = os.path.join(steam_path, 'steamapps', 'libraryfolders.vdf')
    
    with open(library_folders_path, 'r', encoding='utf-8') as f:
        libraries = vdf.load(f)

    games = []

    for library in libraries['libraryfolders'].values():
        steamapps_path = os.path.join(library['path'], 'steamapps')
        for item in os.listdir(steamapps_path):
            if item.endswith('.acf'):

                with open(os.path.join(steamapps_path, item), 'r', encoding='utf-8') as f:
                    game_info = vdf.load(f)
                    games.append(game_info['AppState']['appid'])
    
    return games

def launch_random_game(games):
    random_game_id = random.choice(games)
    subprocess.run(['steam', f'steam://run/{random_game_id}'])


steam_path = ' zadejte cestu k: share/Steam/'

games = get_installed_games(steam_path)
if games:
    launch_random_game(games)
else:
    print("Nebyly nalezeny žádné nainstalované hry.")
