import React, { useState } from 'react'
import './App.css';
import axios from 'axios';
import { TextareaAutosize } from '@mui/base';
import { Button } from '@mui/material';
import { CircularProgress, Typography, Box, Grid2 } from '@mui/material';

function App() {
    const [text, setText] = useState("")
    const [numberWords, setNumberWords] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState('')

    const handleCountWordClick = async () => {
        setLoading(true)
        try {
            const response = await axios.post('http://localhost:8000/word/', { text })
            setNumberWords(response.data.number)
        } catch (error) {
            console.log(error)
            setError(error?.response?.data?.detail?.message || 'Something wrong happen!')
        } finally {
            setLoading(false)
        }
    }

    const handleCleanInput = async () => {
        setText("")
        setNumberWords(null)
        setError('')
    }

  return (
    <Box className="App" sx={{ padding: 3}}>
        <Typography variant="h4" gutterBottom> Count Number of Words </Typography>
        <TextareaAutosize
            placeholder="Enter an text to count the number of words"
            minRows={10}
            maxLength={1000}
            value={text}
            onChange={(event) => setText(event.target.value)}
            style={{ width: '50%', padding: '10px', fontSize: '16px', marginTop: '20px'}}
        />
        <Grid2 spacing={2} alignItems="center" justifyContent="flex-start" sx={{ marginTop: 2 }}>
            <Grid2>
                <Button variant="contained" color="primary" onClick={handleCountWordClick}>
                    { loading ? <CircularProgress size={20} />: 'Submit' }
                </Button>
                <Button variant="contained" color="secondary" onClick={handleCleanInput} sx={{ margin: 2 }}>
                    { 'Clean Text' }
                </Button>
            </Grid2>
            <Grid2>
                {numberWords !== null && (
                    <Typography variant="h6" color="success">
                        Word Count: {numberWords}
                    </Typography>
                )}
            </Grid2>
        </Grid2>
        {error && (
            <Typography collor="red" sx={{ marginTop: 5 }}> {error} </Typography>
        )}
    </Box>
  );
}

export default App;
