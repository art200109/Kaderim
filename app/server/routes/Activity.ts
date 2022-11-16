import express from 'express';

const activityRouter = express.Router();

activityRouter.get('/activities', (req, res, next) => {
  res.send('This is the homepage request');
});

export default activityRouter;
