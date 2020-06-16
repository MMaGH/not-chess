let inputValue = '';

export const dom = function(){
    document.addEventListener('keydown', saveInput);
    movement();
};

function saveInput(e) {
    let acceptableInput = [37, 38, 39, 40];
    if (acceptableInput.includes(e.keyCode)) {
        inputValue = e.keyCode
    }
}


function movement() {
    switch (inputValue) {

        case 37: //left

            break;

        case 39: //right
            break;

        case 38: //up

            break;
        case 40: //down

            break;
    }
}