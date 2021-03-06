import React from 'react';

export const CourtLines = () => {
    return (
        <g>
            <polyline className="baseline-and-corner-three" points="470,140 470,0 30,0 30,140"></polyline>
            <rect width="160" height="190" x="170"></rect>
            <line x1="310" y1="190" x2="310" y2="0"></line>
            <line x1="190" y1="190" x2="190" y2="0"></line>
            {/* Restricted area is 4 feet from baseline */}
            <path className="restricted-area" d="M211,53 c3,22,23,37,44,34c18-2,32-16,34-34"></path>
            <path className="key-bottom" d="M190,190 c0,33,27,60,60,60c33,0,60-27,60-60"></path>
            <path className="key-top" fill="none" strokeDasharray="12.92 10.24" d="M310,190c0-33-27-60-60-60c-33,0-60,27-60,60"></path>
            <line className="right-lane-hash" x1="335" y1="70" x2="330" y2="70"></line> {/* 7 feet from baseline, 6 inches wide */}
            <line className="right-lane-hash" x1="335" y1="80" x2="330" y2="80"></line> {/* 8 feet from baseline */}
            <line className="right-lane-hash" x1="335" y1="110" x2="330" y2="110"></line> {/* 11 feet from baseline */}
            <line className="right-lane-hash" x1="335" y1="140" x2="330" y2="140"></line> {/* 14 feet from baseline */}
            <line className="left-lane-hash" x1="165" y1="70" x2="170" y2="70"></line> {/* 7 feet from baseline, 6 inches wide */}
            <line className="left-lane-hash" x1="165" y1="80" x2="170" y2="80"></line> {/* 8 feet from baseline, 6 inches wide */}
            <line className="left-lane-hash" x1="165" y1="110" x2="170" y2="110"></line> {/* 11 feet from baseline, 6 inches wide */}
            <line className="left-lane-hash" x1="165" y1="140" x2="170" y2="140"></line> {/* 14 feet from baseline, 6 inches wide */}
            {/* 3 point line has parallel lines 3' from sidelines and an arc of 23'4" from the middle of the basket */}
            <line className="left-break-hash" x1="0" x2="30" y1="280" y2="280"></line> {/* break hash is 28 feet from the baseline and extends 3 ft onto the court */}
            <line className="right-break-hash" x1="470" x2="500" y1="280" y2="280"></line>
            <path fill="none" className="three-point-line-center" d="M30,140 c50,122,190,180,310,130c60-24.9,106-71,130-130"></path>
        </g>
    );
};

export default CourtLines;

