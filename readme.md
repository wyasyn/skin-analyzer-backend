### Make shell executable

```bash
chmod +x start.sh
```

### Run with

```bash
./start.sh
```

### Run fastapi

```bash
fastapi dev main.py
```

### Reload .bashrc

```bash
source ~/.bashrc
```

## 🛠️ Build the Docker Image

```bash
docker build -t skin-analyzer .
```

## 🏷️ Tag the Image with Your Docker Hub Username

```bash
docker tag skin-analyzer yasyn/skin-analyzer:latest
```

## 🚀 Push to Docker Hub

```bash
docker push yasyn/skin-analyzer:latest
```

## 🚀 Run the container

```bash
docker run -d -p 80:80 yasyn/skin-analyzer:latest
```

## Running with compose

```bash
docker-compose up --build
```

## From Image on hub

## Star containers

```bash
docker-compose up --build
```

## Stop containers

```bash
docker-compose down
```
