from helpers import *
import engine
import ui
import end_game
import hero_info
import duel

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
# PLAYER_NAME = input("What is your name?")  # to change
# PLAYER_RACE = input("What is your race?")  # to change - zamiast inputa wywołanie funkcji zwracającej rasę
PLAYER_CLASS = input("What is your class?")  # to change - zamiast inputa wywołanie funkcji zwracającej klasę
# PLAYER_CHARACTER = input("What is your character?")  # to change - zamiast inputa wywołanie funkcji zwracającej charakter


BOARD_WIDTH = 80
BOARD_HEIGHT = 30
map_elements = []

CONTROL_DICT = {
    'w':[-1,0],
    's':[1,0],
    'a':[0,-1],
    'd':[0,1]
}


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    # player position and look
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON

    # player stats
    player['HP'] = 25
    player['MANA'] = 10
    player['STR'] = 20
    player['DEX'] = 15
    player['CON'] = 10
    player['INT'] = 10
    player['WIS'] = 10
    player['CHA'] = 10
    
    # hero_info.hero.name = PLAYER_NAME
    # hero_info.hero.race = PLAYER_RACE
    hero_info.hero.hero_class = PLAYER_CLASS
    # hero_info.hero.character = PLAYER_CHARACTER
    return player


def hero_items():
    items = {"Weapon": [], "Armour": [], "Potions": []}
    if PLAYER_CLASS == "wizzard":
        items["Weapon"] = ["Wand"]
        items["Armour"] = ["Leather helmet"]
    elif PLAYER_CLASS == "knight":
        items["Weapon"] = ["Sword"]
        items["Armour"] = ["Helmet", "Shield", "Heavy armour"]
    elif PLAYER_CLASS == "rouge":
        items["Weapon"] = ["Daggers"]
        items["Armour"] = ["Leather helmet", "Leather armour"]
    return items

# def stats_to_list(player):
#     stats_list=[]
#     for key, value in player():
#         stats_list.append(f'{key}: {value}')
#     return stats_list

def change_position(movement, player, board):

    y_pos = 0
    x_pos = 1

    new_y = player['y'] + movement[y_pos]
    new_x = player['x'] + movement[x_pos]

    if board[new_y][new_x] == '#':
        map_ele = '.'
        pass
    else:
        map_ele = board[new_y][new_x]
        player['y'] += movement[0]
        player['x'] += movement[1]
    
    if board[new_y][new_x] == 'S': 
        duel.duel_menu(player)
        map_ele = 'x'
        # check if player is dead and move - alive->move dead->finish
    if board[new_y][new_x] == 'N':
        ui.display_dialog_window('hello')
        key_pressed()

    return map_ele


def play_game(player, board):
    while True:
        key = key_pressed().lower()
        # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        # stats_list = stats_to_list(player)
        last_position = [player['y'], player['x']]
        hero_statistics = hero_info.actual_stats
        hero = hero_info.list_hero_stats(hero_statistics)
        items = hero_items()
        if key == 'q':
            break
        elif key == 'i':
            clear_screen()
            while True:
                ui.display_items(items)
                key = key_pressed().lower()
                if key == 'q':
                    break
        elif key == 'z':
            clear_screen()
        elif key in 'wsad':
            map_elements.insert(0, change_position(CONTROL_DICT[key], player, board))
            board = engine.put_player_on_board(board, player, map_elements, last_position)
        clear_screen()
        if player['HP'] <= 0:
            break
        
        ui.display_board(board, hero)
        print(player['HP'])


def main():
    clear_screen()
    ui.display_dialog_window("Hello Adventurer!")
    player = create_player()

    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    board = engine.read_map('map.txt')
    board = engine.put_player_on_board(board, player, map_elements)
    hero_statistics = hero_info.actual_stats
    hero = hero_info.list_hero_stats(hero_statistics)
    ui.display_board(board, hero)

    play_game(player, board)

    if player['HP'] <= 0:
        end = 'die'
    else:
        end = 'win'  # the 'end' depends from the life of Necromancer-rat
    end_game.end_game(end)  # the parameters: 'win' or 'lose'
    restart_game()

def restart_game():
    print('restart y/n?')
    key = key_pressed()
    if key == 'y':
        main()
    else:
        print('bb')



if __name__ == '__main__':
    main()