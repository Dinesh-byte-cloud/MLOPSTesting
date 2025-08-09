from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

MODEL_PATH = os.path.join("Ml_pipeline","Models","fake_news_models.pkl")
VECTORIZER_PATH = os.path.join("Ml_pipeline","Models","vectorizer.pkl")

print("Current working dir:", os.getcwd())
print("Model path:", MODEL_PATH)
print("Vectorizer path:", VECTORIZER_PATH)
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)  # You need this too!
app = FastAPI()

class NewsItem(BaseModel): #Define input schema
    text:str


@app.get("/")
def read_root():
    return{"message": "Fake News API is up and running!"}

@app.post("/predict")
def predict_news(item:NewsItem):
    text_vectorized = vectorizer.transform([item.text])
    prediction = model.predict(text_vectorized)

    top_features = text_vectorized.nonzero()[1] #for debugging
    feature_words = [vectorizer.get_feature_names_out()[i] for i in top_features]
    print("Model sees these words:", feature_words)
    
    label = "Fake" if prediction[0] == 1 else "Real"
    return{"prediction": label}



