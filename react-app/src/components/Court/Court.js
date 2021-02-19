import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { getShotsByPlayerId } from "../../store/shots";
import ShotMark from '../ShotMark/shotMark'
import { getLeagueAverages } from '../../store/leagueAverages';
import { getPlayerById } from '../../store/player';
import { Zone } from '../Zone/Zone';
import { EfficiencyLegend } from '../EfficiencyLegend/EfficiencyLegend'
import { CourtLines } from '../CourtLines/CourtLines';
import { Hoop } from '../Hoop/Hoop';



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
            <Hoop />
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