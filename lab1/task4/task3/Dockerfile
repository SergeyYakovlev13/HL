FROM node:latest
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN npm install -g json-server
CMD ["json-server", "-H", "0.0.0.0", "-p", "3000",  "-w", "db.json"]