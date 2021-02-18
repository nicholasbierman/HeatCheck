import React from 'react';
import { useSelector } from 'react-redux';


export const CourtTitle = () => {
    const player = useSelector(state => state.player.player);

    return (
        <h1>{ player.first_name } {player.last_name }</h1>
    )
}