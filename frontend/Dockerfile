# --------------------
# Development Stage
# --------------------
    FROM node:18-alpine AS dev

    # Set the working directory
    WORKDIR /app
    
    # Copy package files and install dependencies
    COPY package*.json ./
    RUN npm install
    
    # Copy the rest of the source code
    COPY . .
    
    # Set environment variable for development
    ENV APP_ENV=development
    
    # Expose port for the React development server
    EXPOSE 3000
    
    # Use CMD to start the development server (npm start supports hot-reload)
    CMD ["npm", "start"]
    
    # --------------------
    # Production Build Stage
    # --------------------
    FROM node:18-alpine AS build
    
    WORKDIR /app
    
    # Copy package files and install dependencies
    COPY package*.json ./
    RUN npm install
    
    # Copy all source code
    COPY . .
    
    # Build the production bundle (creates a 'build' folder)
    RUN npm run build
    
    # --------------------
    # Production Final Stage
    # --------------------
    FROM nginx:alpine AS prod
    
    # Remove the default Nginx configuration
    RUN rm /etc/nginx/conf.d/default.conf
    
    # Copy your custom Nginx configuration into the container
    # (Make sure you create a nginx.conf file in your frontend folder)
    COPY nginx.conf /etc/nginx/conf.d
    
    # Copy the production build from the build stage to Nginx's html folder
    COPY --from=build /app/build /usr/share/nginx/html
    
    # Expose port 80 for serving the production build
    EXPOSE 80
    
    # Start Nginx in the foreground
    CMD ["nginx", "-g", "daemon off;"]
    