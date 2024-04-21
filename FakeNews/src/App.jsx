import { useState } from 'react'
import './App.css'
import TextInput from './components/TextInput.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Fake News</h1>
      <TextInput />
      <p className="disclaimer">Disclaimer: The result is not 100% accurate.</p>
    </>
  )
}

export default App
