FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies inside container (not using your local venv)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (excluding .dockerignore entries like venv/)
COPY . .

# Expose Streamlit’s default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
