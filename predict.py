import joblib
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved model from the file
loaded_model = joblib.load('best_model.pkl')

# Load the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Now you can use loaded_model to predict the label of new text
# Preprocess the new text
new_text = "Your new text goes here"
preprocessed_text = preprocess_text(new_text)

# Feature Extraction
new_text_tfidf = tfidf_vectorizer.transform([preprocessed_text])

# Model Prediction
predicted_label = loaded_model.predict(new_text_tfidf)

if predicted_label == 0:
    print("The new text is classified as TRUE news.")
else:
    print("The new text is classified as FAKE news.")
