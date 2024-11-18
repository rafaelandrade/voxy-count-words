import React, { useEffect, useState } from 'react'
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState("")

  useEffect(() => {
    axios.get('http://localhost:8000').then(response => setMessage(response.data.message)).catch(error => console.error(error))
  })

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  );
}

export default App;
