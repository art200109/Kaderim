#Build Steps
FROM node:alpine3.10 as build-step

RUN mkdir /app
WORKDIR /app

COPY client/package.json /app
RUN npm install --legacy-peer-deps
COPY . /app
WORKDIR /app/client

RUN npm run build --transpile-only

#Run Steps
FROM nginx:1.19.8-alpine
COPY --from=build-step /app/client/build /usr/share/nginx/html
