my_map = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '11', 'E', 'C', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', '21', 'X'],
    ['X', 'E', 'X', 'E', 'X', 'B', 'X', 'B', 'X', 'B', 'X', 'E', 'X', 'E', 'X'],
    ['X', 'S', 'E', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'E', 'E', 'X'],
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


def show_bomb(state, user_id):
    if '0' not in my_map[state[0]][state[1]]:
        my_map[state[0]][state[1]] += ',0' + user_id
    print(my_map)


def create_character(nickname, user_id):  # id még kell dolgozni, hogy az is autogeenrált legyen 1-4 között
    new_character = {'name': nickname, 'user_id': str(user_id), 'bomb_count': 1, 'bomb_size': 2, 'life': 1}
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
