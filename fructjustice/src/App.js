import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Navigate, Outlet} from "react-router-dom";
import MainPage from './pages/GamePage';
import { Fragment } from 'react';


function App() {
  return (
    <Fragment>
      <Navigate to="/game" />
      <Outlet />
    </Fragment>
  )
}

export default App;
