# Base Python image
FROM python:3.11-slim

# Install system dependencies (FFmpeg + others)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install Python deps
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend project
COPY backend/ .

# Expose FastAPI port
EXPOSE 8000

# Development: enable --reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# Run app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
