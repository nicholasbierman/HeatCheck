import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import shots from './shots'
import leagueAverages from './leagueAverages'
import player from './player';
import allPlayers from './allPlayers';
import comparisonPlayer from './comparisonPlayer';
import comparisonShots from './comparisonShots';

const rootReducer = combineReducers({
  shots,
  leagueAverages,
  player,
  allPlayers,
  comparisonPlayer,
  comparisonShots
});

let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;