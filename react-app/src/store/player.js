const SET_PLAYER = 'player/setPlayer'

export const setPlayer = (player) => ({
    type: SET_PLAYER,
    payload: player
});

export const getPlayerById = (id) => async (dispatch) => {
    const response = await fetch(`/api/player/${id}`);
    const data = await response.json();
    dispatch(setPlayer(data))
}

const initialState = { player: {} }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case SET_PLAYER:
            newState = { ...state, player: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;