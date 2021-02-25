const SET_COMPARISON_SHOTS = 'shots/setComparisonShots';

const setComparisonShots = (shots) => ({
    type: SET_COMPARISON_SHOTS,
    payload: shots
})

export const getComparisonShotsByPlayerId = (id) => async (dispatch) => {
    const response = await fetch(`/api/shots/${id}`);
    const data = await response.json();
    dispatch(setComparisonShots(data.shots))
}

const initialState = { comparisonShots: [] }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case SET_COMPARISON_SHOTS:
            newState = { ...state, comparisonShots: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;