import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Court } from './components/Court/Court';
import { NavBar } from './components/NavBar/NavBar.js';
import { CourtTitle } from './components/CourtTitle/courtTitle.js'
import { ChangePlayerButton } from './components/ChangePlayerButton/ChangePlayerButton';
import { PlayerSelector } from './components/PlayerSelector/PlayerSelector';
import { Zone } from './components/Zone/Zone';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/">
          <NavBar />
          <ChangePlayerButton />
          <PlayerSelector />
          <CourtTitle />
          <Court />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
