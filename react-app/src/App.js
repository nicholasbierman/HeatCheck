import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { Court } from './components/Court'

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/">
          <h1>HeatCheck</h1>
          <Court />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
