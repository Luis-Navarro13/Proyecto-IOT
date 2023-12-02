import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import PaginaGraficaI from './paginas/PaginaGraficaI';
import PaginaGraficaII from './paginas/PaginaGraficaII';
import PaginaGraficaIII from './paginas/PaginaGraficaIII';
import Controles from './paginas/Controles';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./index.css";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/PaginaGraficaI" element={<PaginaGraficaI />} />
      <Route path="/PaginaGraficaII" element={<PaginaGraficaII />} />
      <Route path="/PaginaGraficaIII" element={<PaginaGraficaIII />} />
      <Route path="/Controles" element={<Controles />} />
    </Routes>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
