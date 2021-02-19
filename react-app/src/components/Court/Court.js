import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getShotsByPlayerId } from "../../store/shots";
import ShotMark from '../ShotMark/shotMark'
import { getLeagueAverages } from '../../store/leagueAverages';
import { getPlayerById } from '../../store/player';
import { Zone } from '../Zone/Zone';
import { EfficiencyLegend } from '../EfficiencyLegend/EfficiencyLegend'
import { CourtLines } from '../CourtLines/CourtLines';

export const Court = () => {
    const shots = useSelector(state => state.shots.shots);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getShotsByPlayerId(201939))
        dispatch(getLeagueAverages())
        dispatch(getPlayerById(201939))
    }, [ dispatch ])
    
    return (
        <div>
            <svg stroke="gray" fill="none" viewBox="0 0 500 470">
            <CourtLines />
            <g className="hoop">
                <line className="backboard" x1="280" y1="40" x2="220" y2="40"></line> {/* 4 feet from baseline, measures 6' horizontally */}
                    <path stroke="orange" className="rim" d="M250,55 c4,0,7-3,7-7c0-4-4-7-7-7c-4,0-7.197,3-7,7 C243,52,246,55,250,55z"></path>
                </g>
            <g>
                    { shots && shots.map((shot, i) => {
                        if (shot.shot_made_flag) {
                            return (
                                <ShotMark key={ i }x={ shot.x } y={ shot.y } />
                            )
                        }
                        return null;
                })}
                </g>
                <EfficiencyLegend />
            </svg>
        </div>

    )
}