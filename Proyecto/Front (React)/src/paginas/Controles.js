import 'C:/Users/luisn/OneDrive/Escritorio/3/IoT/Proyecto2/PaginaInicio/src/App.css';
import Buttons from 'C:/Users/luisn/OneDrive/Escritorio/3/IoT/Proyecto2/PaginaInicio/src/Buttons.js';
import Grid from '@mui/material/Unstable_Grid2'; // Grid version 2
import Botonescontrol from '../BotonControl.jsx';
function PaginaGraficaI() {
  return (
  <div>
    <Grid container spacing={0} style={{ marginLeft: '120px' }}>
      <Grid xs={1}>
        <Buttons />
      </Grid>
      <Grid xs={10}>
        <div className='Rectangulogris' style={{justifyContent:'center'}} >
          
          <h1 className="texto">Controles</h1>
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

            <div className='Rectanguloblanco' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
              <Botonescontrol/>
            </div>
          </div>
        </div>
      </Grid>
    </Grid>
  </div>
  );
}

export default PaginaGraficaI;

