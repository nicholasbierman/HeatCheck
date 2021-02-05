const SET_PLAYER_SHOTS = 'shots/setPlayerShots'

const setPlayerShots = (shots) => ({
    type: SET_PLAYER_SHOTS,
    payload: shots
})

export const getShotsByPlayerId = (id) => async (dispatch) => {
    console.log('HITTING THUNK')
    const response = await fetch(`/api/shots/${id}`);
    const data = await response.json();
    dispatch(setPlayerShots(data.shots))
}

const initialState = { shots: [] }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case SET_PLAYER_SHOTS:
            newState = { ...state, shots: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;