import { useEffect, useState } from 'react';
import Grid from '@mui/material/Unstable_Grid2';
import Box from '@mui/material/Box';
import { LineChart } from '@mui/x-charts/LineChart';
import axios from 'axios';
function ChartI() {
  const [presiones, setPresiones] = useState([]);
  const [presionesData, setPresionesData] = useState([]);
  const [presionesLabels, setPresionesLabels] = useState([]);
  function getPresiones() {
    axios.get('https://primal-turbine-406015.uc.r.appspot.com/presiones').then((response) => {
      console.log(response.data);
      setPresiones(response.data);
      
    })
  }

  useEffect(() => {
    getPresiones();
  }, [])

  useEffect(() => {
    if(presiones.length === 0) return;
    setPresionesData(presiones.map((presion) => presion.presion));
    setPresionesLabels(presiones.map((presion) => presion.fecha));
  }, [presiones])

  return (
      <div>
        <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={0}>
            <Grid xs={12} md={12}>
              {presionesLabels.length>0 &&
                <LineChart
                  width={900}
                  height={300}
                  series={[
                    { data: presionesData, label: 'Presiones',color:"red" },
                  ]}
                  xAxis={[{ scaleType: 'point', data: presionesLabels }]}
                />
              }

            </Grid>
          </Grid>
        </Box>
      </div>
  );
}

export default ChartI;
