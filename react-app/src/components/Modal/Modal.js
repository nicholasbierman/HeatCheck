import React from 'react';
import profile_picture from './github_profile_picture.jpg';

export const Modal = () => {
    return (
        <div style={{
            display: "fixed", zIndex: "1", maxWidth: "10%", maxHeight: "10%"
        }}>
            <p>Hello from Modal!</p>
        </div>
    )
}