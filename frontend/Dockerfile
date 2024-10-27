FROM node:alpine AS build

COPY package.json ./package.json
RUN npm install
COPY . .
RUN npm run build

