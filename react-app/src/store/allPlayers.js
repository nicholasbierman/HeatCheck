const GET_ALL_PLAYERS = 'allPlayers/getAllPlayers'

const setAllPlayers = (players) => ({
    type: GET_ALL_PLAYERS,
    payload: players
});

export const getAllPlayers = () => async (dispatch) => {
    const response = await fetch('/api/player/all');
    const data = await response.json();
    dispatch(setAllPlayers(data.allPlayers));
}

const initialState = { allPlayers: [] }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case GET_ALL_PLAYERS:
            newState = { ...state, allPlayers: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;