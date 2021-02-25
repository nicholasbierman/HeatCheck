import React from 'react';

export const ShotMark = ({ x, y }) => {
    return (
            <rect rx="1" height="5px" width="5px" fill="lime" x={ x } y={ y }>

            </rect>
    )
}

export default ShotMark;