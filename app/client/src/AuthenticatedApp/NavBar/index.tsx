import { AppBar, Grid, Toolbar, Typography } from '@mui/material';
import Greeting from './Greeting';
import ColorModeButton from './ColorModeButton';

interface NavBarProps {
  height: string;
}

const NavBar = ({ height }: NavBarProps) => (
  <AppBar position='relative' sx={{ height, minWidth: '620px' }}>
    <Toolbar>
      <Grid
        container
        flexWrap='nowrap'
        alignItems='center'
        justifyContent='space-between'>
        <Grid container flexWrap='nowrap' sx={{ width: 'auto' }}>
          <Grid item>
            <Typography variant='h5' marginRight='10px'>
              ניהול תורנויות
            </Typography>
          </Grid>
          <Grid
            container
            justifyContent='space-around'
            alignItems='center'
            wrap='nowrap'
            sx={{ width: 'auto', height: '100%' }}></Grid>
        </Grid>
        <Grid
          container
          sx={{ width: 'auto' }}
          alignItems='baseline'
          flexWrap='nowrap'>
          <Greeting />
          <ColorModeButton />
        </Grid>
      </Grid>
    </Toolbar>
  </AppBar>
);

export default NavBar;
