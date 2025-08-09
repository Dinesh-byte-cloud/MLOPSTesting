import mlflow
import mlflow.sklearn
import os
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess import prepare_data

os.makedirs("Models",exist_ok=True)

def train_model():
    x_train,x_test,y_train,y_test,vectorizer = prepare_data()

    clf = PassiveAggressiveClassifier(max_iter = 1000)
    clf.fit(x_train,y_train)
    pred = clf.predict(x_test)

    acc = accuracy_score(y_test,pred)

    with mlflow.start_run():  #start mlflow logging
        mlflow.log_param("model_type","PassiveAggressiveClassifier")
        mlflow.log_metric("accuracy",acc)
        mlflow.log_param("vectorizer","TF-IDF")
        #save model and vectorizer

        joblib.dump(clf,"Models/fake_news_models.pkl") #Saves both the trained classifier and the text vectorizer to disk so they can be loaded later for making predictions on new data.
        joblib.dump(vectorizer,"Models/vectorizer.pkl")

        mlflow.sklearn.log_model(clf,"model")

        print("Accuracy",acc)
        print(classification_report(y_test,pred))
        report = classification_report(y_test,pred)
        #log the classification report as an artifact. 
        with open("TruthWatch/Ml_pipeline/Models/classification_report.txt","w") as f:
            f.write(report)
        mlflow.log_artifact("TruthWatch/Ml_pipeline/Models/classification_report.txt")

        mlflow.set_experiment("FakeNewsDetection") #Experiment name for organizing multiple runs
        mlflow.log_artifact("TruthWatch/Ml_pipeline/Models/vectorizer.pkl") #for logging vectorizer as an artifact for effective tracking


if __name__=="__main__":
    train_model()
