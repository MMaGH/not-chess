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

symbols = {
    'X': 'wall',
    'E': 'empty',
    'B': 'box',
}


def step_player(player_state, player_next):
    my_map[player_next[0]-1][player_next[1]-1] = '1' + player_next[2]
    my_map[player_state[0]-1][player_state[1]-1] = 'E'
    return my_map
