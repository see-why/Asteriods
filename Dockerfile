# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Install system dependencies required for Pygame
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-mixer-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the game files
COPY . .

# Set environment variable for Pygame to run headless
ENV SDL_VIDEODRIVER=dummy
ENV SDL_AUDIODRIVER=disk

# Command to run the game
CMD ["python", "main.py"] 