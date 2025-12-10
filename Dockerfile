# Use Node 20 (Required for Next.js 15)
FROM node:20-alpine

WORKDIR /app

# Copy package config
COPY package.json ./

# Install dependencies
# We use --legacy-peer-deps to avoid potential conflicts with RC versions in a lab setup
RUN npm install --legacy-peer-deps

# Copy application code
COPY app ./app

# Disable Next.js telemetry
ENV NEXT_TELEMETRY_DISABLED=1

# Expose port
EXPOSE 3000

# Start in dev mode to see error logs clearly
CMD ["npm", "run", "dev"]
