import pandas as pd
import nltk
# Perfect! I can see the issue now. You're currently using the global Python interpreter (~\AppData\Local\Programs\Python\Python313\python.exe), but you need to select your virtual environment interpreter.
# Solution:
# I don't see your venv interpreter in the list, so we need to add it manually:
# Do ctrl+shift+p
# Click on "Enter interpreter path..."
# Navigate to your virtual environment Python executable:

# Path: C:\Users\DINESH KRISHNA\OneDrive\Desktop\MLops\TruthWatch\venv\Scripts\python.exe
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

def load_and_clean_data():
    fake = pd.read_csv('C:/Users/DINESH KRISHNA/OneDrive/Desktop/MLops/TruthWatch/Data/FakeData.csv')
    true = pd.read_csv('C:/Users/DINESH KRISHNA/OneDrive/Desktop/MLops/TruthWatch/Data/TrueData.csv')
    fake['label'] = 0  #Fake
    true['label'] = 1 #Real
    data = pd.concat([fake,true])
    data = data.sample(frac=1).reset_index(drop=True) #Shuffle
    return data

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    text = ' '.join([words for words in text.split() if words not in stop_words])
    return text

def prepare_data():
    data = load_and_clean_data()
    data['text'] = data['text'].apply(preprocess_text)

    x = data['text']
    y = data['label']

    vectorizer = TfidfVectorizer(max_df =0.7) #the max_df ensures that words that appears more than 70% of the doc are ignored like the,is etc. TF - how often a words appears and IDF - how rare and uncommon a word is across a doc
    x_vec = vectorizer.fit_transform(x) #Each row = one document/text sample. Each column = one unique word from the vocabulary. Values = TF-IDF scores
    x_train,x_test,y_train,y_test = train_test_split(x_vec,y,test_size = 0.2,random_state = 42)

    return x_train,x_test,y_train,y_test,vectorizer




