import {playerMove, refreshMap} from "./data_handler.js";


export function dom() {
    document.addEventListener('keydown', playerMovement);
    refreshMap(showMap);
}

function playerMovement(e) {
    let playerNode = document.querySelector('[data-playernumber="1"]');
    let playerRowIndex = parseInt(playerNode.dataset.row);
    let playerColIndex = parseInt(playerNode.dataset.col);
    let playerState = [playerRowIndex, playerColIndex];
    let playerNext = [];
    let acceptableInput = [37, 38, 39, 40];
    if (acceptableInput.includes(e.keyCode)) {
        switch (e.keyCode) {
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

function showMap(data) {
    let map = document.querySelector(".map");
    map.innerHTML = '';
    let row_index = 0;
    for (let row of data) {
        let col_index = 0;
        let divRow = '';
        for (let cell of row) {
            if (cell.length != 2) {
                divRow += `<div class="cell ${symbols[cell]}"></div>`;
            } else {
                divRow += `<div class="cell empty">
                               <div class="player" data-playernumber="${cell[0]}" data-direction="${cell[1]}" data-row="${row_index}" data-col="${col_index}"></div>
                           </div>`;
            }
            col_index++;
        }
        map.insertAdjacentHTML('beforeend',`<div class="row">
                                                            ${divRow}
                                                        </div>`)
        row_index++;
    }
    showCharacters();
}

function showCharacters(){
    let players = document.querySelectorAll('.player');
    for (let player of players){
        player.style.background = `url('/static/assets/player${player.dataset.playernumber}_${directions[parseInt(player.dataset.direction)-1]}.png') no-repeat`;
        player.style.backgroundSize = 'cover';
    }
}


let symbols = {
    'X': 'wall',
    'E': 'empty',
    'B': 'box',
}

let directions = ['up', 'left', 'down', 'right'];