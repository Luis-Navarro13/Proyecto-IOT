import { useEffect, useState } from 'react';
import Grid from '@mui/material/Unstable_Grid2';
import Box from '@mui/material/Box';
import { LineChart } from '@mui/x-charts/LineChart';
import axios from 'axios';
function ChartI() {
  const [temperaturas, setTemperaturas] = useState([]);
  const [temperaturasData, setTemperaturasData] = useState([]);
  const [temperaturasLabels, setTemperaturasLabels] = useState([]);
  function getTemperaturas() {
    axios.get('https://primal-turbine-406015.uc.r.appspot.com/temperaturas').then((response) => {
      console.log(response.data);
      setTemperaturas(response.data);
      
    })
  }

  useEffect(() => {
    getTemperaturas();
  }, [])

  useEffect(() => {
    if(temperaturas.length === 0) return;
    setTemperaturasData(temperaturas.map((temperatura) => temperatura.temperatura));
    setTemperaturasLabels(temperaturas.map((temperatura) => temperatura.fecha));
  }, [temperaturas])

  return (
      <div>
        <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={0}>
            <Grid xs={12} md={12}>
              {temperaturasLabels.length>0 &&
                <LineChart
                  width={900}
                  height={300}
                  series={[
                    { data: temperaturasData, label: 'Temperatura',color:"red"},
                  ]}
                  xAxis={[{ scaleType: 'point', data: temperaturasLabels, angle: 100 }]}
                />
              }

            </Grid>
          </Grid>
        </Box>
      </div>
  );
}

export default ChartI;
