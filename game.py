import time
import random
import os
import persistance as ps
import threading

characters_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'characters.csv')
map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'map.csv')

original_map = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '11', 'E', 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', '21', 'X'],
    ['X', 'E', 'X', 'E', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'E', 'X', 'E', 'X'],
    ['X', 'E', 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', 'X'],
    ['X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X'],
    ['X', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
    ['X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X'],
    ['X', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
    ['X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X'],
    ['X', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
    ['X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'B', 'X'],
    ['X', 'E', 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', 'X'],
    ['X', 'E', 'X', 'E', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'E', 'X', 'E', 'X'],
    ['X', '31', 'E', 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', '41', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

symbols = {
    'X': 'wall',
    'E': 'empty',
    'B': 'box',
    'C': 'count_upgrade',
    'S': 'size_upgrade',
}


def initialize_my_map():
    ps.export_map(map_path, original_map)


def step_player(player_state, player_next, character_list, character_name):
    my_map = ps.get_map(map_path)
    tile_list = my_map[player_next[0]][player_next[1]].split(',')
    invalid_slots = ['B', 'X']
    current_character = get_current_player(character_list, character_name)
    valid = True
    for tile in tile_list:
        if tile in invalid_slots:
            valid = False
            break
    if valid:
        update_character(character_list, character_name, my_map[player_next[0]][player_next[1]])
        my_map[player_next[0]][player_next[1]] = my_map[player_next[0]][player_next[1]].replace('C', 'E')
        my_map[player_next[0]][player_next[1]] = my_map[player_next[0]][player_next[1]].replace('S', 'E')
        my_map[player_next[0]][player_next[1]] = my_map[player_next[0]][player_next[1]].replace('E', (
                    current_character['user_id'] + player_next[2]))
        for i in range(1, 5):
            my_map[player_state[0]][player_state[1]] = my_map[player_state[0]][player_state[1]].replace(
                str(current_character['user_id']) + str(i), 'E')
        ps.export_map(map_path, my_map)


def show_bomb(state, user_id, character_list, character_name):
    my_map = ps.get_map(map_path)
    current_character = get_current_player(character_list, character_name)
    if ('0' not in my_map[state[0]][state[1]]) and (
            int(current_character['bomb_used']) < int(current_character['bomb_count'])):
        my_map[state[0]][state[1]] += ',0' + str(user_id)
        ps.export_map(map_path, my_map)
        th1 = threading.Thread(target=bomb_animation, args=[state, user_id, character_name])
        th1.start()


def bomb_animation(state, user_id, character_name):
    character_list = ps.get_characters(characters_path)
    current_character = get_current_player(character_list, character_name)
    current_character['bomb_used'] = str(int(current_character["bomb_used"]) + 1)
    ps.export_characters(characters_path, character_list)
    time.sleep(2)
    my_map = ps.get_map(map_path)
    my_map[state[0]][state[1]] = my_map[state[0]][state[1]].replace((',0' + str(user_id)), (',M' + str(user_id)), 1)
    explosion_placement(0, 1, current_character, state, user_id, 'R', my_map)
    explosion_placement(0, -1, current_character, state, user_id, 'L', my_map)
    explosion_placement(1, 0, current_character, state, user_id, 'D', my_map)
    explosion_placement(-1, 0, current_character, state, user_id, 'U', my_map)
    ps.export_map(map_path, my_map)
    bomb_delete_animation(state, user_id, character_name)


def bomb_delete_animation(state, user_id, character_name):
    time.sleep(1)
    character_list = ps.get_characters(characters_path)
    current_character = get_current_player(character_list, character_name)
    my_map = ps.get_map(map_path)
    my_map[state[0]][state[1]] = my_map[state[0]][state[1]].replace((',M' + str(user_id)), '', 1)
    remove_explosion_placement(0, 1, current_character, state, user_id, 'R', my_map)
    remove_explosion_placement(0, -1, current_character, state, user_id, 'L', my_map)
    remove_explosion_placement(1, 0, current_character, state, user_id, 'D', my_map)
    remove_explosion_placement(-1, 0, current_character, state, user_id, 'U', my_map)
    current_character['bomb_used'] = str(int(current_character["bomb_used"]) - 1)
    ps.export_characters(characters_path, character_list)
    ps.export_map(map_path, my_map)


def explosion_placement(i, j, current_character, state, user_id, direction, my_map):
    while int(current_character['bomb_size']) >= i >= -1 * int(current_character['bomb_size']) and int(
            current_character[
                'bomb_size']) >= j >= -1 * int(current_character['bomb_size']):
        target = my_map[state[0] + i][state[1] + j]
        if 'X' not in target:
            target_list = target.split(',')
            for item in target_list:
                if item[0] in ['1', '2', '3', '4']:
                    my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace(item, 'E')
            my_map[state[0] + i][state[1] + j] += ',' + direction + user_id
            if 'B' in target:
                number = random.randint(1, 4)
                if number == 1:
                    my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace('B', random.choice(
                        ['C', 'S']))
                else:
                    my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace('B', 'E')
                break
        else:
            break
        if i < 0:
            i -= 1
        elif 0 < i:
            i += 1
        if j < 0:
            j -= 1
        elif 0 < j:
            j += 1


def remove_explosion_placement(i, j, current_character, state, user_id, direction, my_map):
    while int(current_character['bomb_size']) >= i >= -1 * int(current_character['bomb_size']) and int(
            current_character['bomb_size']) >= j >= -1 * int(current_character['bomb_size']):
        if 'X' not in my_map[state[0] + i][state[1] + j]:
            my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace(
                (',' + direction + str(user_id)), '', 1)
        else:
            break
        if i < 0:
            i -= 1
        elif 0 < i:
            i += 1
        if j < 0:
            j -= 1
        elif 0 < j:
            j += 1


def create_character(nickname, user_id):
    new_character = {'name': nickname, 'user_id': str(user_id), 'bomb_used': 0, 'bomb_count': 1, 'bomb_size': 2,
                     'life': 1}
    return new_character


def update_character(character_list, character_name, upgrade_type):
    current_character = get_current_player(character_list, character_name)
    if 'C' in upgrade_type:
        current_character['bomb_count'] = str(int(current_character["bomb_count"]) + 1)
    elif 'S' in upgrade_type:
        current_character['bomb_size'] = str(int(current_character["bomb_size"]) + 1)
    return None


def get_current_player(character_list, character_name):
    current_character = {}
    for character in character_list:
        if character['name'] == character_name:
            current_character = character
    return current_character
