import time
import random

my_map = [
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


def step_player(player_state, player_next, bomb, character_list, character_name):
    tile = my_map[player_next[0]][player_next[1]]
    valid_slots = ['E', 'C', 'S']
    current_character = get_current_player(character_list, character_name)
    if tile in valid_slots:
        update_character(character_list, character_name, tile)
        if bomb:
            my_map[player_next[0]][player_next[1]] = current_character['user_id'] + player_next[2]
            my_map[player_state[0]][player_state[1]] = 'E,0' + current_character['user_id']
        else:
            my_map[player_next[0]][player_next[1]] = current_character['user_id'] + player_next[2]
            my_map[player_state[0]][player_state[1]] = 'E'


def show_bomb(state, user_id, character_list, character_name):
    current_character = get_current_player(character_list, character_name)
    if ('0' not in my_map[state[0]][state[1]]) and (current_character['bomb_used'] < current_character['bomb_count']):
        current_character['bomb_used'] += 1
        my_map[state[0]][state[1]] += ',0' + str(user_id)
        bomb_animation(state, user_id, current_character)


def bomb_animation(state, user_id, current_character):
    time.sleep(2)
    my_map[state[0]][state[1]] = my_map[state[0]][state[1]].replace((',0' + str(user_id)), (',M' + str(user_id)))
    explosion_placement(0, 1, current_character, state, user_id, 'R')
    explosion_placement(0, -1, current_character, state, user_id, 'L')
    explosion_placement(1, 0, current_character, state, user_id, 'D')
    explosion_placement(-1, 0, current_character, state, user_id, 'U')
    time.sleep(1)
    current_character['bomb_used'] -= 1
    my_map[state[0]][state[1]] = my_map[state[0]][state[1]].replace((',M' + str(user_id)), '')
    remove_explosion_placement(0, 1, current_character, state, user_id, 'R')
    remove_explosion_placement(0, -1, current_character, state, user_id, 'L')
    remove_explosion_placement(1, 0, current_character, state, user_id, 'D')
    remove_explosion_placement(-1, 0, current_character, state, user_id, 'U')


def explosion_placement(i, j, current_character, state, user_id, direction):
    while current_character['bomb_size'] >= i >= -1 * current_character['bomb_size'] and current_character['bomb_size'] >= j >= -1 * current_character['bomb_size']:
        target = my_map[state[0] + i][state[1] + j]
        if 'X' not in target:
            my_map[state[0] + i][state[1] + j] += ',' + direction + user_id
            if 'B' in target:
                number = random.randint(1, 4)
                if number == 1:
                    my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace('B', random.choice(['C', 'S']))
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


def remove_explosion_placement(i, j, current_character, state, user_id, direction):
    while current_character['bomb_size'] >= i >= -1 * current_character['bomb_size'] and current_character['bomb_size'] >= j >= -1 * current_character['bomb_size']:
        my_map[state[0] + i][state[1] + j] = my_map[state[0] + i][state[1] + j].replace((',' + direction + str(user_id)), '')
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
    if upgrade_type == 'C':
        current_character['bomb_count'] += 1
    elif upgrade_type == 'S':
        current_character['bomb_size'] += 1
    return None


def get_current_player(character_list, character_name):
    current_character = {}
    for character in character_list:
        if character['name'] == character_name:
            current_character = character
    return current_character
