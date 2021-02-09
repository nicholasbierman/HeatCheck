const SET_LEAGUE_AVERAGES = 'leagueAverages/setLeagueAverages';

const setLeagueAverages = (leagueAverages) => ({
    type: SET_LEAGUE_AVERAGES,
    payload: leagueAverages
})

export const getLeagueAverages = () => async (dispatch) => {
    const response = await fetch()
}