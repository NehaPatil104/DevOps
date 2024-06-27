# Build stage
FROM node as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --configuration=production

# Production stage
FROM nginx as production-stage
COPY --from=build-stage /app/dist/my-angular-app /usr/share/nginx/html

