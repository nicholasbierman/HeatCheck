import React from 'react';

export const Court = () => {
    return (
        <svg stroke="orange" fill="purple" viewBox="0 0 500 470">
            <g fill="white" stroke="green" strokeWidth="5">
            </g>
            <g class="court">
                <polyline fill="none" stroke="#999999" strokeLinecap="square" strokeLinejoin="bevel" strokeMiterlimit="10" viewBox="0 0 440 140" points="470,140 470,0 30,0 30,147">
                </polyline>
                <rect width="160" height="190" x="170"></rect>
                <line x1="310" y1="190" x2="310" y2="0"></line>
                <line x1="190" y1="190" x2="190" y2="0"></line>
                <path d="M190,190 c0,33,27,60,60,60c33,0,60-27,60-60"></path>
            </g>
        </svg>
    )
}