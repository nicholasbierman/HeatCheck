import React from 'react';
import { useSelector } from 'react-redux';


export const CourtTitle = () => {
    const player = useSelector(state => state.player.player);
    const shots = useSelector(state => state.shots.shots);

    return (
        <>
            <h1 style={ { color: "whitesmoke" } }>{ player.first_name } {player.last_name } | 2020-2021 Regular Season | {shots.length } Shots</h1>
        </>
    )
}