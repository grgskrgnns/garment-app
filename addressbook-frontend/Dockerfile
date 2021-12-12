FROM node:14.5.0-alpine
WORKDIR /app/frontend
COPY package.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
EXPOSE 3000