import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import MainPage from './pages/GamePage';
import Profile from './pages/ProfilePage';
import Shop from './pages/ShopPage';


const root = ReactDOM.createRoot(document.getElementById('root'));
const routers = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
    children: [
      {
        path: "/profile",
        element: <Profile />
      },
      {
        path: "/fruct-shop",
        element: <Shop />
      }
    ]
  }
])

root.render(
	<React.StrictMode>
    <RouterProvider router={routers}/>
	</React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
