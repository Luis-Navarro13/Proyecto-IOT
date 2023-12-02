
import { useEffect, useState } from 'react';
import axios from 'axios';
function App() {
  const [presiones, setPresiones] = useState([]);
  function getPresiones() {
    axios.get('https://primal-turbine-406015.uc.r.appspot.com/presiones').then((response) => {
      console.log(response.data);
      setPresiones(response.data);
      
    })
  }

  useEffect(() => {
    getPresiones();
  }, [])

  return (
    <>
  <p>Presiones:</p>
  <ul>
    {presiones.slice(-10).map((presion, index) => (
      <li key={index}>
        Fecha: {presion.fecha}, Presion: {presion.presion}
      </li>
    ))}
  </ul>
    </>
  );
};

export default App;
