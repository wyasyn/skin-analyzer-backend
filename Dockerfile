# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=300 -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 8000

# Run the FastAPI app using fastapi-cli
CMD ["fastapi", "run"]
