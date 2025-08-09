#Base image
FROM python:3.13-slim
#Set working directory
WORKDIR /app
#Copy requirements first and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#Copy entire project (excluding venv via .dockerignore)
COPY . .
#Expose Fast api port
EXPOSE 8000
#Start FastAPI
CMD ["uvicorn","api.main:app","--host","0.0.0.0","--port","8000"]


