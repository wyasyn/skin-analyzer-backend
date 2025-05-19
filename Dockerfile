# Base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/app/.cache/huggingface \
    TRANSFORMERS_CACHE=/app/.cache/huggingface/transformers \
    HF_HUB_CACHE=/app/.cache/huggingface/hub \
    PORT=8000

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# Download model during build
RUN python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='yasyn14/skin-analyzer', filename='model-v1.keras', cache_dir='/app/.cache')"

# Copy rest of your code
COPY . .

# Expose port
EXPOSE ${PORT}

# Start FastAPI app using the PORT env
CMD ["sh", "-c", "fastapi run main.py --host 0.0.0.0 --port $PORT"]
