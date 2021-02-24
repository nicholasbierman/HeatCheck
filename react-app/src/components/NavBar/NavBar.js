import React from 'react';
import { NavLink } from 'react-router-dom';

export const NavBar = () => {
  return (
    <nav style={ { height: "fit-content", color: "whitesmoke", margin: "0 0 60px 0", display: "flex", backgroundColor: "orange", width: "100%" } }>
      <ul style={ { listStyle: "none", display: "flex", alignItems: "center", width: "100%", justifyContent: "start" } }>
        <li style={{marginRight: "10%", fontSize: "30px"}}>HeatCheck<span role="img"></span>🔥✅</li>
        <NavLink to="/" style={{textDecoration: "none", color: "whitesmoke"}}><li><button style={{}}>Charts</button></li></NavLink>
      </ul>
    </nav>
  );
}