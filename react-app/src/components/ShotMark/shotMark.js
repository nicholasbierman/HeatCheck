import React from 'react';

export const ShotMark = ({ x, y }) => {
    return (
        <rect height="10px" width="10px" color="green" fill="green" x={ x } y={ y }>

        </rect>
    )
}

export default ShotMark;