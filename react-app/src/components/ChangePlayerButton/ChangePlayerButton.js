import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { setPlayer } from '../../store/player';

export const ChangePlayerButton = () => {
    const dispatch = useDispatch();
    const allPlayers = useSelector(state => state.allPlayers.allPlayers);
    const [ selectedPlayer, setSelectedPlayer ] = useState(null);
    useEffect(() => {
        console.log('SELECTED PLAYER CHANGED', selectedPlayer)
    }, [selectedPlayer])
    return (
        <form onSubmit={ () => setPlayer(selectedPlayer)}>
            <select onChange={(e) => setSelectedPlayer(e.target.value) }>
                { allPlayers.map((player, i) => {
                    return <option key={ i } value={player.nba_player_id}>{ player.first_name } { player.last_name }</option>
                })}
            </select>
        <button style={{backgroundColor: "blueviolet", borderColor: "transparent", cursor: "pointer", borderRadius: "4px", width: "10%", }}>Change Player
        </button>
        </form>
    )
}