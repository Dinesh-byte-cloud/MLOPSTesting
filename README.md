# TruthWatch - Fake News Detection API

A machine learning-powered REST API built with FastAPI to detect fake news articles. The application uses trained models to classify news text as either "Fake" or "Real" based on textual analysis.

## Features

- 🔍 **Real-time News Classification**: Classify news articles as fake or real
- 🚀 **FastAPI Framework**: High-performance, automatic API documentation
- 🐳 **Docker Support**: Containerized deployment for consistency across environments
- 📊 **ML Pipeline**: Uses trained machine learning models with vectorization
- 📝 **Interactive Documentation**: Swagger UI for easy API testing
- 🔧 **Debug Features**: Provides feature analysis for model predictions

## Project Structure

```
TruthWatch/
├── api/
│   └── main.py              # FastAPI application
├── Mlpipeline/
│   └── Models/
│       ├── fake_news_models.pkl    # Trained ML model
│       └── vectorizer.pkl          # Text vectorizer
├── Data/                    # Training data (if applicable)
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── .dockerignore          # Docker ignore file
└── README.md              # This file
```

## Prerequisites

- Python 3.13+
- Docker (optional, for containerized deployment)
- Required Python packages (see requirements.txt)

## Installation & Setup

### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd TruthWatch
   ```

2. **Build the Docker image**
   ```bash
   docker build -t fake-news-api .
   ```

3. **Run the container**
   ```bash
   docker run -d -p 8000:8000 fake-news-api
   ```

4. **Verify the deployment**
   ```bash
   docker ps
   docker logs <container-id>
   ```

### Option 2: Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd TruthWatch
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   cd api
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## API Usage

### Base URL
- Local: `http://localhost:8000`
- Docker: `http://localhost:8000`

### Endpoints

#### 1. Health Check
- **GET** `/`
- **Description**: Check if the API is running
- **Response**: 
  ```json
  {
    "message": "Fake News API is up and running!"
  }
  ```

#### 2. Predict News Classification
- **POST** `/predict`
- **Description**: Classify news text as fake or real
- **Request Body**:
  ```json
  {
    "text": "Your news article text here"
  }
  ```
- **Response**:
  ```json
  {
    "prediction": "Fake"  // or "Real"
  }
  ```

### Testing the API

#### Using Interactive Documentation (Recommended)
1. Navigate to `http://localhost:8000/docs`
2. Click on the `/predict` endpoint
3. Click "Try it out"
4. Enter your JSON data
5. Click "Execute"

#### Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Breaking news: Scientists discover new planet in our solar system"}'
```

#### Using JavaScript/Fetch
```javascript
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: "Your news article text here"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Docker Commands Reference

```bash
# Build the image
docker build -t fake-news-api .

# Run container in background
docker run -d -p 8000:8000 fake-news-api

# Run container interactively (for debugging)
docker run -it -p 8000:8000 fake-news-api

# View running containers
docker ps

# View container logs
docker logs <container-id>

# Stop container
docker stop <container-id>

# Remove container
docker rm <container-id>

# Remove image
docker rmi fake-news-api
```

## Development

### Model Information
- The API uses pre-trained machine learning models stored in `Mlpipeline/Models/`
- `fake_news_models.pkl`: The trained classification model
- `vectorizer.pkl`: Text vectorization model for feature extraction

### Adding New Features
1. Modify `api/main.py` for new endpoints
2. Update `requirements.txt` for new dependencies
3. Rebuild Docker image if using containerized deployment

### Debugging
The application includes debug features that log:
- Model file paths and loading status
- Feature words extracted from input text
- Current working directory information

## Troubleshooting

### Common Issues

1. **Container fails to start**
   - Check logs: `docker logs <container-id>`
   - Verify model files exist in `Mlpipeline/Models/`
   - Ensure all dependencies are in `requirements.txt`

2. **Method Not Allowed Error**
   - Use POST request for `/predict` endpoint
   - Include proper JSON headers
   - Use interactive docs at `/docs` for testing

3. **Model loading errors**
   - Verify model files are present and accessible
   - Check file paths in logs
   - Ensure models are compatible with current scikit-learn version

4. **Port already in use**
   - Stop existing containers: `docker stop <container-id>`
   - Use different port: `docker run -d -p 8001:8000 fake-news-api`

## API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Technologies Used

- **FastAPI**: Web framework for building APIs
- **scikit-learn**: Machine learning models
- **joblib**: Model serialization
- **uvicorn**: ASGI server
- **Docker**: Containerization
- **Python 3.13**: Programming language

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

