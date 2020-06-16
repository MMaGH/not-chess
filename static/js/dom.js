import {playerMove} from "./data_handler.js";


export function dom(){
    document.addEventListener('keydown', playerMovement);

}

function playerMovement(e) {
    let playerNode = document.querySelector('[data-player="1"]');
    let playerRowIndex = parseInt(playerNode.dataset.row);
    let playerColIndex = parseInt(playerNode.dataset.col);
    let playerState = [playerRowIndex, playerColIndex];
    let playerNext = [];
    let acceptableInput = [37, 38, 39, 40];
    if (acceptableInput.includes(e.keyCode)) {
        switch (e.keyCode){
            case 37: // left
                playerNext = [playerRowIndex, playerColIndex - 1, '1'];
                break;
            case 39: // right
                playerNext = [playerRowIndex, playerColIndex + 1, '2'];
                break;
            case 38: // up
                playerNext = [playerRowIndex - 1, playerColIndex, '3'];
                break;
            case 40: // down
                playerNext = [playerRowIndex + 1, playerColIndex, '4'];
                break;
        }
        playerMove(playerState, playerNext, changePlayerPosition);
    }
}

function changePlayerPosition() {

}
