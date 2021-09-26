FROM node:16.6
WORKDIR /code
COPY package*.json /code/
RUN npm install
ENV NUXT_HOST 0.0.0.0
COPY . .