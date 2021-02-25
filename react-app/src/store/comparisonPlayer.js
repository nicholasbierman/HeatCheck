const SET_COMPARISON_PLAYER = 'comparisonPlayer/setComparisonPlayer'

export const setComparisonPlayer = (player) => ({
    type: SET_COMPARISON_PLAYER,
    payload: player
});

export const getComparisonPlayerById = (id) => async (dispatch) => {
    const response = await fetch(`/api/player/${id}`);
    const data = await response.json();
    dispatch(setComparisonPlayer(data))
}

const initialState = { comparisonPlayer: {} }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case SET_COMPARISON_PLAYER:
            newState = { ...state, comparisonPlayer: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;