FROM node:alpine as build

COPY package.json package.json
RUN cd app
RUN npm install
COPY . .
RUN npm run build

