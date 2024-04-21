import React, { useState } from 'react';
import axios from 'axios';
import './TextInput.css';

function TextInput() {
  const [newsText, setNewsText] = useState('');
  const [prediction, setPrediction] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const handleTextChange = (e) => {
    setNewsText(e.target.value);
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    setPrediction('');
    setErrorMessage('');

    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', { text: newsText });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error predicting:', error);
      setErrorMessage('Failed to get prediction. Please try again later.');
    } finally {
      setIsLoading(false);
    }
  };

  const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };

  return (
    <div className="text-input-container">
      <textarea
        className="text-input"
        rows="20"
        cols="100"
        placeholder="Enter news text..."
        value={newsText}
        onChange={handleTextChange}
      />
      <br />
      <button className="submit-button" onClick={handleSubmit} disabled={isLoading}>
        {isLoading ? 'Predicting...' : 'Predict'}
      </button>
      {errorMessage.length > 0 && <div style={{ 
            color: 'black',
            padding: 10,
            }}>{errorMessage}</div>}
      {prediction && (
        <div style={{
            color: 'black',
            padding: 10,
        }}>
          {`Prediction: ${capitalizeFirstLetter(prediction)}`}
        </div>
      )}
    </div>
  );
}

export default TextInput;
