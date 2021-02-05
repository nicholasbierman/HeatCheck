import React from 'react';

export const Court = () => {
    return (
        <svg stroke="orange" viewBox="0 0 500 470">
            <g class="court">
                <polyline class="backboard-and-corner-three" fill="none" stroke="#999999" strokeLinecap="square" strokeLinejoin="bevel" strokeMiterlimit="10" viewBox="0 0 440 140" points="470,140 470,0 30,0 30,147">
                </polyline>
                <rect width="160" height="190" x="170"></rect>
                <line x1="310" y1="190" x2="310" y2="0"></line>
                <line x1="190" y1="190" x2="190" y2="0"></line>
                /* Restricted area is 4 feet from baseline */
                <path class="restricted-area" d="M211,53 c3,22,23,37,44,34c18-2,32-16,34-34"></path>
                <path class="key-bottom" d="M190,190 c0,33,27,60,60,60c33,0,60-27,60-60"></path>
                <path class="key-top" fill="none" stroke-dasharray="12.92 10.24" d="M310,190c0-33-27-60-60-60c-33,0-60,27-60,60"></path>
                <line class="right-lane-hash" x1="335" y1="70" x2="330" y2="70"></line> /* 7 feet from baseline, 6 inches wide */
                <line class="right-lane-hash"x1="335" y1="80" x2="330" y2="80"></line> /* 8 feet from baseline */
                <line class="right-lane-hash"x1="335" y1="110" x2="330" y2="110"></line> /* 11 feet from baseline */
                <line class="right-lane-hash"x1="335" y1="140" x2="330" y2="140"></line> /* 14 feet from baseline */
                <line class="left-lane-hash" x1="165" y1="70" x2="170" y2="70"></line> /* 7 feet from baseline, 6 inches wide */
                <line class="left-lane-hash" x1="165" y1="80" x2="170" y2="80"></line> /* 8 feet from baseline, 6 inches wide */
            </g>
        </svg>
    )
}