import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Court } from './components/Court/Court';
import { NavBar } from './components/NavBar/NavBar.js';
import { CourtTitle } from './components/CourtTitle/courtTitle.js'
import { ChangePlayerButton } from './components/ChangePlayerButton/ChangePlayerButton';
import { HalfCourt } from './components/HalfCourt/HalfCourt';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/compare">
          <NavBar />
          <HalfCourt />
          <HalfCourt right={true} />
        </Route>
        <Route path="/">
          <NavBar />
          <Court />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
