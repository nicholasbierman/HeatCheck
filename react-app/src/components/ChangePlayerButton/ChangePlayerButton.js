import React from 'react';
import { useDispatch, useSelector } from "react-redux";
import { getAllPlayers } from '../../store/allPlayers';
export const ChangePlayerButton = () => {
    const dispatch = useDispatch();
    const allPlayers = useSelector(state => state.allPlayers.allPlayers);

    return (
        <form>
            <select>
                { allPlayers.map((player, i) => {
                    return <option key={ i } value={player.nba_player_id}>{ player.first_name } { player.last_name }</option>
                })}
            </select>
        <button style={{backgroundColor: "blueviolet", borderColor: "transparent", cursor: "pointer", borderRadius: "4px", width: "10%", }}>Change Player
        </button>
        </form>
    )
}