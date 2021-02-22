import React from 'react';
import { getAllPlayers } from '../../store/allPlayers';
export const ChangePlayerButton = () => {
    return (
        <button style={{backgroundColor: "blueviolet", borderColor: "transparent", cursor: "pointer", borderRadius: "4px", width: "10%", }}>
            Change Player
        </button>
    )
}