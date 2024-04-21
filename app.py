from flask import Flask, request, jsonify
from flask_cors import CORS 
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import joblib
from preprocessing import preprocess_text

true_df = pd.read_csv('./archive/True.csv')
fake_df = pd.read_csv('./archive/Fake.csv')

true_df['label'] = 0
fake_df['label'] = 1

df = pd.concat([true_df, fake_df])
df = df.sample(frac=1).reset_index(drop=True)
df.drop(['subject', 'date'], axis=1, inplace=True)
X = df[["title", "text"]]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train["title"] + " " + X_train["text"])
X_test_tfidf = tfidf_vectorizer.transform(X_test["title"] + " " + X_test["text"])

model = RandomForestClassifier()
model.fit(X_train_tfidf, y_train)

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods=['POST'])
def predict():
    new_text = request.json['text']
    preprocessed_text = preprocess_text(new_text)
    new_text_tfidf = tfidf_vectorizer.transform([preprocessed_text])
    predicted_label = model.predict(new_text_tfidf)
    confidence_score = model.predict_proba(new_text_tfidf)[0][predicted_label[0]] * 100

    return jsonify({'prediction': 'fake' if predicted_label == 1 else 'real', 'confidence_score': confidence_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
