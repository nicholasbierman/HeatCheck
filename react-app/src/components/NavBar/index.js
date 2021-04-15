import React from 'react';
import { NavLink } from 'react-router-dom';
import logo from './heatcheck_logo.png';
import { ModalContainer } from '../ModalContainer/ModalContainer';

export const NavBar = () => {
  return (
    <nav style={{ color: "whitesmoke", height: "4.75em", margin: "0 0 60px 0", display: "flex", backgroundColor: "#fe5500", width: "100%" }}>
      <ul style={{ listStyle: "none", display: "flex", height: "fit-content", alignItems: "center", width: "100%", justifyContent: "start" }}>
        <li style={{ marginRight: "15%", fontSize: "30px" }}><img src={logo} alt="HeatCheck Logo" width="250px" height="60px"></img></li>
        <NavLink to="/" style={{ marginRight: "5%", textDecoration: "none", color: "whitesmoke" }}><li><button style={{ marginBottom: "10px", padding: ".5em", borderRadius: "5px", color: "#4fbfa8", backgroundColor: "#ffffff", borderColor: "transparent", cursor: "pointer", fontWeight: "bold", letterSpacing: "0.05em", transition: "all 0.4s ease 0s" }}>Charts</button></li></NavLink>
        <NavLink to="/compare" style={{ textDecoration: "none", color: "whitesmoke" }}><li><button style={{ marginBottom: "10px", padding: "0.5em", borderRadius: "5px", color: "#4fbfa8", backgroundColor: "#ffffff", borderColor: "transparent", cursor: "pointer", fontWeight: "bold", letterSpacing: "0.05em", transition: "all 0.4s ease 0s" }}>Compare</button></li></NavLink>
      </ul>
      <ModalContainer />
    </nav>
  );
};

export default NavBar;