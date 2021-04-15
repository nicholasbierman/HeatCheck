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
import { ChangePlayerButton } from "../ChangePlayerButton/ChangePlayerButton";
import { getComparisonPlayerById } from '../../store/comparisonPlayer';
import { getComparisonShotsByPlayerId } from '../../store/comparisonShots';


export const HalfCourt = ({ comparison }) => {
    const shots = useSelector(state => state.shots.shots);
    const comparisonShots = useSelector(state => state.comparisonShots.comparisonShots);
    const dispatch = useDispatch();


    useEffect(() => {
        dispatch(getShotsByPlayerId(201939));
        dispatch(getComparisonShotsByPlayerId(201939));
        dispatch(getLeagueAverages());
        dispatch(getPlayerById(201939));
        dispatch(getComparisonPlayerById(201935));
    }, [ dispatch ]);
    
    return (
        <div style={{ backgroundColor: "black", width: "50%", display: "inline-block" }}>
            <ChangePlayerButton comparison={comparison} />
            <svg maxWidth="100%" stroke="gray" fill="none" viewBox="0 0 500 470">
                <CourtLines />
                <Hoop />
                <g stroke="slategray" strokeWidth="0.4px">
                    {!comparison ? shots && shots.map((shot, i) => {
                        if (shot.shot_made_flag) {
                            return (
                                <ShotMark comparison={comparison} key={i} x={shot.x} y={shot.y} />
                            );
                        }
                        return null;
                    }) : comparisonShots && comparisonShots.map((shot, i) => {
                        if (shot.shot_made_flag) {
                            return (
                                <ShotMark comparison={comparison} key={i} x={shot.x} y={shot.y} />
                            );
                        }
                        return null;
                    })}
                </g>
                <Zone />
                <EfficiencyLegend />
            </svg>
        </div>
    );
};

export default HalfCourt;