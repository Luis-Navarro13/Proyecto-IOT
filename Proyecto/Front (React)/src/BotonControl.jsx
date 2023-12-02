import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

import { ReactComponent as AdelanteIcon } from './svg/adelante.svg';
import { ReactComponent as AtrasIcon } from './svg/atras.svg';
import { ReactComponent as DetenerIcon } from './svg/detener.svg';
function BotonControl() {
  const [adelanteSeleccionado, setAdelanteSeleccionado] = useState(false);
  const [atrasSeleccionado, setAtrasSeleccionado] = useState(false);
  const [detenerSeleccionado, setdetenerSeleccionado] = useState(false);

  const toggleAdelanteSeleccion = () => {
    setAdelanteSeleccionado(!adelanteSeleccionado);
    setAtrasSeleccionado(false);
    setdetenerSeleccionado(false);
    console.log("0");
  };

  const toggleAtrasSeleccion = () => {
    setAdelanteSeleccionado(false);
    setAtrasSeleccionado(!atrasSeleccionado);
    setdetenerSeleccionado(false);
    console.log("1");
  };
  const toggledetenerSeleccion = () => {
    setAdelanteSeleccionado(false);
    setAtrasSeleccionado(false);
    setdetenerSeleccionado(!detenerSeleccionado);
    console.log("2");
  };
  return (
    <div>

        <button
          className={adelanteSeleccionado ? 'boton-mover-seleccionado' : 'boton-mover'}
          style={{
            position: 'absolute',
            top: 100,
            left: 400,
            cursor: 'pointer',
          }}
          onClick={toggleAdelanteSeleccion}
          >
          <AdelanteIcon />
        </button>

        <button className={atrasSeleccionado ? 'boton-mover-seleccionado' : 'boton-mover'}         style={{
          position: 'absolute',
          top:380,
          left:400,
          cursor: 'pointer'}}
          onClick={toggleAtrasSeleccion}><AtrasIcon/>
            </button>
        <button className={detenerSeleccionado ? 'boton-detener-seleccionado' : 'boton-detener'}         style={{
          position: 'absolute',
          top:100,
          left:840,
          cursor: 'pointer'}}
          onClick={toggledetenerSeleccion}><DetenerIcon/>
          </button>
    </div>
  );
}

export default BotonControl;
