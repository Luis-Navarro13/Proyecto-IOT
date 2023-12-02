import './App.css';
import Buttons from './Buttons';
import Grid from '@mui/material/Unstable_Grid2'; // Grid version 2
import Image from './Imagen.js';
function App() {
  return (
    <div>
    <Grid container spacing={0} style={{ marginLeft: '120px' }}>
      <Grid xs={1}>
        <Buttons />
      </Grid>
      <Grid xs={10}>
        <div className='Rectangulogris' style={{justifyContent:'center'}} >
          
          <h1 className="texto">Reporte de XROVER</h1>
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

            <div className='Rectanguloblanco' style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
              <Image/>
            </div>
          </div>
        </div>
      </Grid>
    </Grid>
  </div>
  );
};

export default App;
