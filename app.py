from flask import Flask, request, jsonify
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

# Load the saved model from the file
loaded_model = joblib.load('best_model.pkl')

# Load the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

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
    predicted_label = loaded_model.predict(new_text_tfidf)

    # Return the prediction result as JSON
    return jsonify({'prediction': 'fake' if predicted_label == 1 else 'real'})

if __name__ == '__main__':
    app.run(debug=True)
