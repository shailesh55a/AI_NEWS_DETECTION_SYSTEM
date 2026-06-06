# Using official Pyhton image
FROM python:3.11-slim

# Prevent Pyhton from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensures logs appera immediately
ENV PYTHONNUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Streamlit port
EXPOSE 8501

# start application
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
