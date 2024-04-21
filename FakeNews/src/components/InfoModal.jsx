import React from 'react';
import Modal from 'react-modal';
import './InfoModal.css';

function InfoModal({ isOpen, onClose }) {
  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      contentLabel="Modal"
      className="modal"
      overlayClassName="modal-overlay"
    >
      <div className="modal-header">
        <h2>Why Detecting Fake News Is Important</h2>
        <button className="close-button" onClick={onClose}>X</button>
      </div>
      <div className="modal-content">
        <p>In today's digital age, the proliferation of fake news has become a significant concern. Fake news can spread rapidly through social media and other online platforms, leading to misinformation and confusion among the public. Detecting and combating fake news is essential to maintaining an informed society and preserving the integrity of information sources.</p>
        <p>Older individuals, particularly those less familiar with digital media and technology, may be more vulnerable to false information and hoaxes circulating online. They may lack the digital literacy skills to critically evaluate news sources and identify misinformation. As a result, they are more susceptible to believing and sharing fake news, which can have serious consequences for their understanding of current events and decision-making processes. Therefore, raising awareness and providing education about fake news detection is crucial, especially among older populations.</p>
      </div>
    </Modal>
  );
}

export default InfoModal;
