import { useState } from 'react'
import './App.css'
import TextInput from './components/TextInput.jsx'
import InfoModal from './components/InfoModal.jsx'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faQuestion } from '@fortawesome/free-solid-svg-icons'

function App() {
  const [showModal, setShowModal] = useState(false);

  const toggleModal = () => {
    setShowModal(!showModal);
  };

  return (
    <>
      <h1>CheckMate</h1>
      <p className="subtitle">Check your news sources</p>
      <div className="question-icon" onClick={toggleModal}>
       <FontAwesomeIcon icon={faQuestion} size="2xl"/>
      </div>
      <TextInput />
      <p className="disclaimer">Disclaimer: The result is not 100% accurate.</p>
      <InfoModal isOpen={showModal} onClose={toggleModal} />
    </>
  )
}

export default App
