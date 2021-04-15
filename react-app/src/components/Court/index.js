import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getShotsByPlayerId } from "../../store/shots";
import ShotMark from '../ShotMark'
import { getLeagueAverages } from '../../store/leagueAverages';
import { getPlayerById } from '../../store/player';
import { Zone } from '../Zone';
import { EfficiencyLegend } from '../EfficiencyLegend'
import { CourtLines } from '../CourtLines';
import { Hoop } from '../Hoop';
import { CourtTitle } from '../CourtTitle';


export const Court = () => {
    const shots = useSelector(state => state.shots.shots);
    const dispatch = useDispatch();
    const [ highlightedZone, setHighlightedZone ] = useState();


    useEffect(() => {
        dispatch(getShotsByPlayerId(201939));
        dispatch(getLeagueAverages());
        dispatch(getPlayerById(201939));
    }, [ dispatch ]);
    
    return (
        <div style={{ backgroundColor: "black" }}>
            <CourtTitle />
            <svg max-height="fit-content" stroke="gray" fill="none" viewBox="0 0 500 470">
                <CourtLines />
                <Hoop />
                <g stroke="slategray" strokeWidth="0.4px">
                    {shots && shots.map((shot, i) => {
                        if (shot.shot_made_flag) {
                            return (
                                <ShotMark key={i} x={shot.x} y={shot.y} />
                            );
                        }
                        return null;
                    })}
                </g>
                <Zone />
                {/* <EfficiencyLegend /> */}
            </svg>
        </div>
    );
};

export default Court;