import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import configureStore from './store';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import * as shotActions from './store/shots';

const store = configureStore();

if (process.env.NODE_ENV !== 'production') {
  window.store = store;
  window.shotActions = shotActions;
}

function Root() {
  return (
      <Provider store={store}>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </Provider>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>,
  document.getElementById('root')
);
