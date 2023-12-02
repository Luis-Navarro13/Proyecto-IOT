
import { useEffect, useState } from 'react';
import axios from 'axios';
function App() {
  const [distancias, setDistancias] = useState([]);
  function getDistancias() {
    axios.get('https://primal-turbine-406015.uc.r.appspot.com/distancias').then((response) => {
      console.log(response.data);
      setDistancias(response.data);
      
    })
  }

  useEffect(() => {
    getDistancias();
  }, [])
 
  return (
    <>
  <p>Distancias:</p>
  <ul>
    {distancias.slice(-10).map((distancia, index) => (
      <li key={index}>
        Fecha: {distancia.fecha}, Distancia: {distancia.distancia}
      </li>
    ))}
  </ul>
    </>
  );
};

export default App;
