export const playerMove = async (state, next, bomb) => {
    let dict = {'state': state, 'next': next, 'isBomb': bomb};
    const options = {
        method: 'POST',
        body: JSON.stringify(dict),
        headers: {
            'Content-Type': 'application/json'
        }
    };
    await fetch('/player-move', options);
}

export const getBomb = async (state, userId) => {
    let dict = {'bombState': state, 'userId': userId};
    const options = {
        method: 'POST',
        body: JSON.stringify(dict),
        headers: {
            'Content-Type': 'application/json'
        }
    };
    await fetch('/player-place-bomb', options);
}

export const refreshMap = async (callback) => {
    getMap(callback);
    setInterval(() => getMap(callback), 200);
}

function getMap(callback){
    fetch("/map")
        .then(response => response.json())
        .then(data => callback(data))
}