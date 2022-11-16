import express from 'express';

const userRouter = express.Router();

userRouter.get('/', (req, res, next) => {
  res.send('This is the homepage request');
});

export default userRouter;
