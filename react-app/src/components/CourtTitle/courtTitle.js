import React from 'react';
import { useSelector } from 'react-redux';


export const CourtTitle = () => {
    const player = useSelector(state => state.player.player);
    const shots = useSelector(state => state.shots.shots);

    return (
        <h1>{ player.first_name } {player.last_name } - {shots.length } Shots</h1>
    )
}