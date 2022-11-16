import express from 'express';

import userRouter from './routes/User';
import activityRouter from './routes/Activity';
('./routes/Activity');

// Creating express server
const app = express();

// Handling routes request
app.use('/users', userRouter);
app.use('/activities', activityRouter);
app.listen(3000, () => {
  console.log('Server is Running');
});
