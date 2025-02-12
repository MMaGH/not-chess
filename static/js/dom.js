import {playerMove, refreshMap, getBomb, canMove} from "./data_handler.js";


export function dom() {
    document.addEventListener('keydown', (e) => {
        let map = document.querySelector(".map");
        let userId = map.dataset.playernum;
        let playerNode = document.querySelector(`.player[data-playernumber="${userId}"]`);
        let playerRowIndex = parseInt(playerNode.dataset.row);
        let playerColIndex = parseInt(playerNode.dataset.col);
        let playerState = [playerRowIndex, playerColIndex];

        let playerKeyCode = e.keyCode;
        if (playerKeyCode === 0 || playerKeyCode === 32) {
            placeBomb(playerState, userId);
        } else if (canMove) {
            playerMovement(playerKeyCode, playerRowIndex, playerColIndex, playerState)
        }
    });
    refreshMap(showMap);
}

function playerMovement(playerKeyCode, playerRowIndex, playerColIndex, playerState) {
    let playerNext = [];
    let acceptableInput = [37, 38, 39, 40];
    if (acceptableInput.includes(playerKeyCode)) {
        switch (playerKeyCode) {
            case 37: // left
                playerNext = [playerRowIndex, playerColIndex - 1, '2'];
                break;
            case 39: // right
                playerNext = [playerRowIndex, playerColIndex + 1, '4'];
                break;
            case 38: // up
                playerNext = [playerRowIndex - 1, playerColIndex, '1'];
                break;
            case 40: // down
                playerNext = [playerRowIndex + 1, playerColIndex, '3'];
                break;
        }
        playerMove(playerState, playerNext);
    }
}


function placeBomb(playerState, userId) {
    getBomb(playerState, userId);
}

function showMap(data) {
    let map = document.querySelector(".map");
    map.innerHTML = '';
    let row_index = 0;
    for (let row of data) {
        let col_index = 0;
        let divRow = '';
        for (let cell of row) {
            let cellArr = cell.split(',');
            divRow += '<div class="cell">';
            for (let char of cellArr) {
                if (char in symbols) {
                    divRow += `<div class="${symbols[char]}"></div>`;
                }
                else if (!isNaN(char) && char[0] !== '0') {
                    divRow += `<div class="player" data-playernumber="${char[0]}" data-direction="${char[1]}" data-row="${row_index}" data-col="${col_index}"></div>`;
                }
                else if (!isNaN(char) && char[0] === '0') {
                    divRow += `<div class="bomb" data-playernumber="${char[1]}"></div>`;
                }
                else {
                    divRow += `<div class="fire" data-playernumber="${char[1]}" data-direction="${char[0]}"></div>`;
                }
            }
            divRow += '</div>';
            col_index++;
        }
        map.insertAdjacentHTML('beforeend', `<div class="row">
                                                            ${divRow}
                                                        </div>`)
        row_index++;
    }
    showCharacters();
    showBombs();
    showExplosion();
}

function showCharacters() {
    let players = document.querySelectorAll('.player');
    for (let player of players) {
        player.style.background = `url('/static/assets/player${player.dataset.playernumber}_${directions[parseInt(player.dataset.direction) - 1]}.png') no-repeat`;
        player.style.backgroundSize = 'cover';
    }
}


function showBombs() {
    let bombs = document.querySelectorAll('.bomb');
    for (let bomb of bombs) {
        bomb.style.background = `url('/static/assets/player${bomb.dataset.playernumber}_bomb.png') no-repeat`;
        bomb.style.backgroundSize = 'cover';
    }
}


function showExplosion() {
    let fires = document.querySelectorAll('.fire');
    for (let fire of fires) {
        fire.style.background = `url('/static/assets/player${fire.dataset.playernumber}_bomb_${explosion[fire.dataset.direction][0]}.png') no-repeat`;
        fire.style.backgroundSize = 'cover';
        fire.style.transform = `rotate(${explosion[fire.dataset.direction][1]}deg)`
    }
}

let explosion = {
    'M': ['middle', 0],
    'D': ['edge', 270],
    'U': ['edge', 90],
    'R': ['edge', 180],
    'L': ['edge', 0],
}


let symbols = {
    'X': 'wall',
    'E': 'empty',
    'B': 'box',
    'C': 'count_upgrade',
    'S': 'size_upgrade',
}

let directions = ['up', 'left', 'down', 'right'];
