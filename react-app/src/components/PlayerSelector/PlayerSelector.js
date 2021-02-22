import React, {useEffect} from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllPlayers } from '../../store/allPlayers';

export const PlayerSelector = () => {
    const players = useSelector(state => state.allPlayers.allPlayers);
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getAllPlayers())
    })

    return (
        null
    )
}