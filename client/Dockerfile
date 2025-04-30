# Use official Node.js image as the base image
FROM node:23-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the Next.js app
COPY . /app/

# Expose the frontend port
EXPOSE 3000

# Run the Next.js app
CMD ["npm", "run", "dev"]
