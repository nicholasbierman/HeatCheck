import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { getPlayerById } from '../../store/player';
import { getShotsByPlayerId } from '../../store/shots';
import { getAllPlayers } from '../../store/allPlayers';
import { getComparisonPlayerById } from '../../store/comparisonPlayer';
import { getComparisonShotsByPlayerId } from '../../store/comparisonShots';


export const ChangePlayerButton = ({comparison}) => {
    const dispatch = useDispatch();
    const allPlayers = useSelector(state => state.allPlayers.allPlayers);
    const [ selectedPlayer, setSelectedPlayer ] = useState(null);
    const [ comparisonPlayer, setComparisonPlayer ] = useState(null);

    useEffect(() => {
        dispatch(getPlayerById(selectedPlayer));
        dispatch(getShotsByPlayerId(selectedPlayer));
    }, [dispatch, selectedPlayer]);

    useEffect(() => {
        dispatch(getComparisonPlayerById(comparisonPlayer));
        dispatch(getComparisonShotsByPlayerId(comparisonPlayer));
    }, [dispatch, comparisonPlayer])

    useEffect(() => {
        dispatch(getAllPlayers())
    }, [dispatch])
    
    return (
        <form onSubmit={(e) => e.preventDefault()}>
            <select style={{ backgroundColor: "slategray", borderColor: "transparent", cursor: "pointer", borderRadius: "4px" }} onChange={(e) => comparison ? setComparisonPlayer(e.target.value) : setSelectedPlayer(e.target.value)}>
                {comparison ? <option selected disabled hidden>Compare to...</option> : <option selected disabled hidden>Change Player...</option>}
                {allPlayers.map((player, i) => {
                    return <option key={ i } value={player.nba_player_id}>{ player.last_name }, { player.first_name }</option>
                })}
            </select>
        {/* <button style={{backgroundColor: "blueviolet", borderColor: "transparent", cursor: "pointer", borderRadius: "4px", width: "10%"}}>Change Player
        </button> */}
        </form>
    )
}