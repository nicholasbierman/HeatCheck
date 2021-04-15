import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Court } from './components/Court';
import { NavBar } from './components/NavBar';
import { CourtTitle } from './components/CourtTitle'
import { ChangePlayerButton } from './components/ChangePlayerButton';
import { HalfCourt } from './components/HalfCourt';
import { Footer } from './components/Footer';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/compare">
          <NavBar />
          <HalfCourt />
          <HalfCourt comparison={true} />
        </Route>
        <Route path="/">
          <NavBar />
          <Court />
          <Footer />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
