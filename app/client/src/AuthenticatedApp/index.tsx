import { Route, Routes } from 'react-router-dom';
import Shell from './Shell';
import NotFound from '../components/NotFound';
import Home from './Home';

const ShellRoutes = () => (
  <Routes>
    <Route path='/' element={<Shell />}>
      <Route index element={<Home />} />
      <Route path='*' element={<NotFound />} />
    </Route>
  </Routes>
);

export default ShellRoutes;
