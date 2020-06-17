export const playerMove = async (state, next) => {
    let dict = {'state': state, 'next': next};
    const options = {
        method: 'POST',
        body: JSON.stringify(dict),
        headers: {
            'Content-Type': 'application/json'
        }
    };
    let response = await fetch('/player-move', options);
    let data = await response.json();
}

export const refreshMap = async (callback) => {
    getMap(callback);
    setInterval(() => getMap(callback), 500);
}

function getMap(callback){
    fetch("/map")
        .then(response => response.json())
        .then(data => callback(data))
}