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

# Load the dataset
true_df = pd.read_csv('./archive/True.csv')
fake_df = pd.read_csv('./archive/Fake.csv')

# Assign labels
true_df['label'] = 0
fake_df['label'] = 1

# Concatenate the dataframes
df = pd.concat([true_df, fake_df])

# Shuffle the dataframe
df = df.sample(frac=1).reset_index(drop=True)

# Drop unnecessary columns
df.drop(['subject', 'date'], axis=1, inplace=True)

# Split the data into features and labels
X = df[["title", "text"]]
y = df["label"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train["title"] + " " + X_train["text"])

# Transform the testing data
X_test_tfidf = tfidf_vectorizer.transform(X_test["title"] + " " + X_test["text"])

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train_tfidf, y_train)

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the new text from the request data
    new_text = request.json['text']
    # Preprocess the new text
    preprocessed_text = preprocess_text(new_text)

    # Feature Extraction
    new_text_tfidf = tfidf_vectorizer.transform([preprocessed_text])

    # Model Prediction
    predicted_label = model.predict(new_text_tfidf)

    # Return the prediction result as JSON
    return jsonify({'prediction': 'fake' if predicted_label == 1 else 'real'})

if __name__ == '__main__':
    app.run(debug=True)
