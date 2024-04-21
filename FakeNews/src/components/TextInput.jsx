import React, { useState } from 'react';
import axios from 'axios';

function TextInput() {
  const [newsText, setNewsText] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleTextChange = (e) => {
    setNewsText(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('/predict', { text: newsText });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  return (
    <div>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter news text..."
        value={newsText}
        onChange={handleTextChange}
      />
      <br />
      <button onClick={handleSubmit}>Predict</button>
      {prediction && <div>{`Prediction: ${prediction}`}</div>}
    </div>
  );
}

export default TextInput;
