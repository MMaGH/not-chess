export const playerMove = async (state, next, callback) => {
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
    await callback(data)
}