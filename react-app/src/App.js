import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Court } from './components/Court';
import { NavBar } from './components/NavBar/NavBar.js';
import { CourtTitle } from './components/CourtTitle/courtTitle.js'

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/">
          <NavBar />
          <CourtTitle />
          <Court />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
