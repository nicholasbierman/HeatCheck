import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { getPlayerById } from '../../store/player';
import { getShotsByPlayerId } from '../../store/shots';

export const ChangePlayerButton = () => {
    const dispatch = useDispatch();
    const allPlayers = useSelector(state => state.allPlayers.allPlayers);
    const [ selectedPlayer, setSelectedPlayer ] = useState(null);
    useEffect(() => {
        dispatch(getPlayerById(selectedPlayer))
        dispatch(getShotsByPlayerId(selectedPlayer));
    }, [ selectedPlayer ])
    
    
    return (
        <form onSubmit={(e) => e.preventDefault() }>
            <select style={ {cursor: "pointer"} } onChange={(e) => setSelectedPlayer(e.target.value) }>
                { allPlayers.map((player, i) => {
                    return <option key={ i } value={player.nba_player_id}>{ player.first_name } { player.last_name }</option>
                })}
            </select>
        <button style={{backgroundColor: "blueviolet", borderColor: "transparent", cursor: "pointer", borderRadius: "4px", width: "10%", }}>Change Player
        </button>
        </form>
    )
}