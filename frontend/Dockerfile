# frontend/Dockerfile

FROM node:18-alpine

# Create app directory
WORKDIR /app

# Copy package info and install dependencies
COPY package*.json ./
RUN npm install

# Copy in all your source code
COPY . .

# Expose the dev server port
EXPOSE 3000

# Default command for development
CMD ["npm", "start"]
