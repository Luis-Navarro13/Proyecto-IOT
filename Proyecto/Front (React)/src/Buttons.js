import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { ReactComponent as HomeIcon } from './svg/home.svg';
import { ReactComponent as TimeIcon } from './svg/time.svg';
import { ReactComponent as DistanceIcon } from './svg/distance.svg';
import { ReactComponent as PressureIcon } from './svg/pressure.svg';
import { ReactComponent as ControlIcon } from './svg/control.svg';

function Buttons() {
  const navigate = useNavigate();
  const location = useLocation();
  const [selectedButtons, setSelectedButtons] = useState([false, false, false, false, false]);

  useEffect(() => {
    // Actualizar el estado de los botones según la ubicación actual
    const currentPath = location.pathname;
    const newSelectedButtons = [false, false, false, false, false];
    
    if (currentPath === '/') {
      newSelectedButtons[0] = true;
    } else if (currentPath === '/PaginaGraficaI') {
      newSelectedButtons[1] = true;
    } else if (currentPath === '/PaginaGraficaII') {
      newSelectedButtons[2] = true;
    } else if (currentPath === '/PaginaGraficaIII') {
      newSelectedButtons[3] = true;
    } else if (currentPath === '/Controles') {
      newSelectedButtons[4] = true;
    }

    setSelectedButtons(newSelectedButtons);
  }, [location.pathname]);

  const handleClick = (index, path) => {
    setSelectedButtons(new Array(5).fill(false)); // Reiniciar todos los estados a false
    setSelectedButtons((prev) => ({ ...prev, [index]: true }));
    navigate(path);
  };

  return (
    <div>
      {/* BOTON 1 */}
      <button
        className={selectedButtons[0] ? 'boton-seleccionado' : 'boton-sinseleccionar'}
        style={{
          position: 'absolute',
          top: 60,
          left: 147.5,
          cursor: 'pointer',
        }}
        onClick={() => handleClick(0, '/')}
      >
        <HomeIcon width="78" height="108" />
      </button>

      {/* BOTON 2 */}
      <button
        className={selectedButtons[1] ? 'boton-seleccionado' : 'boton-sinseleccionar'}
        style={{
          position: 'absolute',
          top: 185,
          left: 147.5,
          cursor: 'pointer',
        }}
        onClick={() => handleClick(1, '/PaginaGraficaI')}
      >
        <TimeIcon width="78" height="108" />
      </button>

      {/* BOTON 3 */}
      <button
        className={selectedButtons[2] ? 'boton-seleccionado' : 'boton-sinseleccionar'}
        style={{
          position: 'absolute',
          top: 310,
          left: 147.5,
          cursor: 'pointer',
        }}
        onClick={() => handleClick(2, '/PaginaGraficaII')}
      >
        <DistanceIcon width="78" height="108" />
      </button>

      {/* BOTON 4 */}
      <button
        className={selectedButtons[3] ? 'boton-seleccionado' : 'boton-sinseleccionar'}
        style={{
          position: 'absolute',
          top: 435,
          left: 147.5,
          cursor: 'pointer',
        }}
        onClick={() => handleClick(3, '/PaginaGraficaIII')}
      >
        <PressureIcon width="78" height="108" />
      </button>

      {/* BOTON 5 */}
      <button
        className={selectedButtons[4] ? 'boton-seleccionado' : 'boton-sinseleccionar'}
        style={{
          position: 'absolute',
          top: 560,
          left: 147.5,
          cursor: 'pointer',
        }}
        onClick={() => handleClick(4, '/Controles')}
      >
        <ControlIcon width="78" height="108" />
      </button>
    </div>
  );
}

export default Buttons;
