const SET_LEAGUE_AVERAGES = 'leagueAverages/setLeagueAverages';

const setLeagueAverages = (leagueAverages) => ({
    type: SET_LEAGUE_AVERAGES,
    payload: leagueAverages
})

export const getLeagueAverages = () => async (dispatch) => {
    const response = await fetch('/api/league_averages/')
    const data = await response.json()
    dispatch(setLeagueAverages(data.league_averages))
}

const initialState = { leagueAverages: [] }

function reducer (state = initialState, action) {
    let newState;
    switch (action.type) {
        case SET_LEAGUE_AVERAGES:
            newState = { ...state, leagueAverages: action.payload }
            return newState;
        default:
            return state;
    }
}

export default reducer;