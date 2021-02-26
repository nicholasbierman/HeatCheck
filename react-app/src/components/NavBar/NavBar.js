import React from 'react';
import { NavLink } from 'react-router-dom';
import logo from './heatcheck_logo.png';

export const NavBar = () => {
  return (
    <nav style={ { height: "70px", color: "whitesmoke", margin: "0 0 60px 0", display: "flex", backgroundColor: "#fe5500", width: "100%" } }>
      <ul style={ { listStyle: "none", display: "flex", alignItems: "center", width: "100%", justifyContent: "start" } }>
        <li style={{marginRight: "15%", fontSize: "30px"}}><img src={logo} width="250px" height="60px"></img></li>
        <NavLink to="/" style={{ marginRight: "5%", textDecoration: "none", color: "whitesmoke" }}><li><button style={{ borderRadius: "5px", color: "#4fbfa8", backgroundColor: "#ffffff", borderColor: "transparent", cursor: "pointer", fontWeight: "bold", letterSpacing: "0.05em", transition: "all 0.4s ease 0s" }}>Charts</button></li></NavLink>
        <NavLink to="/compare" style={ { textDecoration: "none", color: "whitesmoke" } }><li><button style={ { borderRadius: "5px", color: "#4fbfa8", backgroundColor: "#ffffff", borderColor: "transparent", cursor: "pointer", fontWeight: "bold", letterSpacing: "0.05em", transition: "all 0.4s ease 0s" } }>Compare</button></li></NavLink>
      </ul>
    </nav>
  );
}