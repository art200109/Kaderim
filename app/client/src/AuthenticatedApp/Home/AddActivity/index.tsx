import 'react-big-calendar/lib/css/react-big-calendar.css';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import ActivitiesStepper from './ActivitiesStepper';

interface AddActivityProps {
  open: boolean;
  handleClose: () => void;
}

const AddActivity = ({ open, handleClose }: AddActivityProps) => {
  return (
    <Dialog open={open} onClose={handleClose}>
      <DialogTitle>הוספת תורנות</DialogTitle>
      <DialogContent>
        <ActivitiesStepper />
      </DialogContent>
    </Dialog>
  );
};

export default AddActivity;
