import { useEffect, useState } from 'react';
import Grid from '@mui/material/Unstable_Grid2';
import Box from '@mui/material/Box';
import { LineChart } from '@mui/x-charts/LineChart';
import axios from 'axios';
function ChartI() {
  const [distancias, setDistancias] = useState([]);
  const [distanciasData, setDistanciasData] = useState([]);
  const [distanciasLabels, setDistanciasLabels] = useState([]);
  function getDistancias() {
    axios.get('https://primal-turbine-406015.uc.r.appspot.com/distancias').then((response) => {
      console.log(response.data);
      setDistancias(response.data);
      
    })
  }

  useEffect(() => {
    getDistancias();
  }, [])

  useEffect(() => {
    if(distancias.length === 0) return;
    setDistanciasData(distancias.map((distancia) => distancia.distancia));
    setDistanciasLabels(distancias.map((distancia) => distancia.fecha));
  }, [distancias])

  return (
      <div>
        <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={0}>
            <Grid xs={12} md={12}>
              {distanciasLabels.length>0 &&
                <LineChart
                  width={900}
                  height={300}
                  series={[
                    { data: distanciasData, label: 'Distancias',color:"red"},
                  ]}
                  xAxis={[{ scaleType: 'point', data: distanciasLabels }]}
                />
              }

            </Grid>
          </Grid>
        </Box>
      </div>
  );
}

export default ChartI;
