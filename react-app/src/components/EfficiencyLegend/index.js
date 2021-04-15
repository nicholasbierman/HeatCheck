import React from 'react';

export const EfficiencyLegend = () => {
    return (
        <g className="efficiency-legend">
            <text x="380" y="445" style={{ fontSize: "12px" }}>Efficiency By Location</text>
            <rect x="380" y="450" width="15" height="15" rx="2" ry="2" fill="rgb(0, 0, 255)"></rect>
            <rect x="400" y="450" width="15" height="15" rx="2" ry="2" fill="rgb(0, 150, 255)"></rect>
            <rect x="420" y="450" width="15" height="15" rx="2" ry="2" fill="rgb(163, 225, 255)"></rect>
            <rect x="440" y="450" width="15" height="15" rx="2" ry="2" fill="gold"></rect>
            <rect x="460" y="450" width="15" height="15" rx="2" ry="2" fill="orange"></rect>
            <rect x="480" y="450" width="15" height="15" rx="2" ry="2" fill="rgb(255, 0, 0)"></rect>
        </g>
    );
};

export default EfficiencyLegend;