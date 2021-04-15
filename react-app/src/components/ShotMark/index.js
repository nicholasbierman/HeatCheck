import React from 'react';

export const ShotMark = ({ x, y, comparison }) => {
    return (
        <rect rx="1" height="5px" width="5px" fill={comparison ? "#FE00FB" : "lime"} x={ x } y={ y }>

            </rect>
    )
}

export default ShotMark;