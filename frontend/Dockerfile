# --------------------
# Development Stage
# --------------------
    FROM node:20-alpine AS dev

    WORKDIR /app
    
    # Copy package files & install dependencies
    COPY package*.json ./
    RUN npm install
    
    # Copy the rest of the source code
    COPY . .
    
    # Dev environment variable
    ENV APP_ENV=development
    
    # Expose port 3000 for dev server
    EXPOSE 3000
    
    # Default command runs the React dev server (with hot reload)
    CMD ["npm", "start"]
    
    # --------------------
    # Production Build Stage
    # --------------------
    FROM node:20-alpine AS build
    
    WORKDIR /app
    
    # Copy package files & install dependencies
    COPY package*.json ./
    RUN npm install
    
    # Copy all source code
    COPY . .
    
    # Build the production bundle (makes a "build" folder)
    RUN npm run build
    
    # --------------------
    # Production Final Stage (Nginx)
    # --------------------
    FROM nginx:alpine AS prod
    
    # Remove default config if needed
    RUN rm /etc/nginx/conf.d/default.conf
    
    # Copy your custom Nginx config
    # Make sure you have a "nginx.conf" in your frontend folder
    COPY nginx.conf /etc/nginx/conf.d
    
    # Copy the built app from the build stage
    COPY --from=build /app/build /usr/share/nginx/html
    
    # Expose port 80 inside container
    EXPOSE 80
    
    # Start Nginx
    CMD ["nginx", "-g", "daemon off;"]
    