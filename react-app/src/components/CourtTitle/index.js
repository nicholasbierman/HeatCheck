import React from 'react';
import { useSelector } from 'react-redux';
import { ChangePlayerButton } from '../ChangePlayerButton/ChangePlayerButton';


export const CourtTitle = () => {
    const player = useSelector(state => state.player.player);
    const shots = useSelector(state => state.shots.shots);

    return (
        <div style={{ width: "75%", margin: "1% 25% 0 25%" }}>
            <ChangePlayerButton />
            <h1 style={{ color: "whitesmoke" }}>{player.first_name} {player.last_name} | 2020-2021 Regular Season | {shots.length} Shots</h1>
        </div>
    );
};

export default CourtTitle;