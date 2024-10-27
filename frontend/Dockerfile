FROM node:alpine as build

RUN cd app
COPY package.json package.json
RUN npm install
COPY . .
RUN npm run build

