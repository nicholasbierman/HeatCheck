import React from 'react';
import { NavLink } from 'react-router-dom';

export const NavBar = () => {
  return (
    <nav style={ { height: "fit-content", color: "whitesmoke", margin: "0 0 60px 0", display: "flex", backgroundColor: "orange", width: "100%" } }>
      <ul style={ { listStyle: "none", display: "flex" } }>
        <li>HeatCheck</li>
        <li>Player Shot Charts</li>
      </ul>
    </nav>
  );
}