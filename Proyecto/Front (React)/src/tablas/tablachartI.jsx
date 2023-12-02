
import { useEffect, useState } from 'react';
import axios from 'axios';
function App() {
    const [temperaturas, setTemperaturas] = useState([]);
    function getTemperaturas() {
      axios.get('https://primal-turbine-406015.uc.r.appspot.com/temperaturas').then((response) => {
        console.log(response.data);
        setTemperaturas(response.data);
        
      })
    }
  
    useEffect(() => {
      getTemperaturas();
    }, [])
  
  return (
    <>
  <p>Temperaturas:</p>
  <ul>
    {temperaturas.slice(-10).map((temperatura, index) => (
      <li key={index}>
        Fecha: {temperatura.fecha}, Temperatura: {temperatura.temperatura}
      </li>
    ))}
  </ul>
    </>
  );
};

export default App;
