import React, { useState } from 'react';

export const Zone = () => {
    const [ highlightedZone, setHighlightedZone ] = useState(false);
    const handleClick = (e) => {
        e.stopPropagation();
        setHighlightedZone(!highlightedZone);
    };
    return (
        <g onClick={(e) => handleClick(e)} style={{ opacity: highlightedZone ? "1" : "0" }} >
            <path id="zone" style={{ fillOpacity: "0.3" }} fill="purple" className="zone right-mid-range" d="M470,140, 470,0, 330,0 330,140"></path>
        </g>
    );
};

export default Zone;