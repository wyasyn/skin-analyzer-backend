# Use official Python slim image
FROM python:3.12-slim

# Set environment variables to improve Python behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 

# Set working directory
WORKDIR /app

# Install system dependencies (optional: can add git, build-essential etc. if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies from a reliable mirror
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port (informational)
EXPOSE $PORT

# Command to run FastAPI app
CMD ["sh", "-c", "fastapi run main.py --host 0.0.0.0 --port ${PORT}"]
