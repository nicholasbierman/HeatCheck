import React from 'react';

export const Hoop = () => {
    return (
        <g className="hoop">
            <line className="backboard" x1="280" y1="40" x2="220" y2="40"></line> {/* 4 feet from baseline, measures 6' horizontally */}
            <path stroke="orange" className="rim" d="M250,55 c4,0,7-3,7-7c0-4-4-7-7-7c-4,0-7.197,3-7,7 C243,52,246,55,250,55z"></path>
        </g>
    );
};

export default Hoop;