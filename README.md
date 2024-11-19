# Voxy Challenge: Word Count Application

This project is a solution for the Voxy challenge. It consists of a backend built with **FastAPI** and a frontend developed using **React**. The goal of this application is to count the number of words in a given sentence.

## Features

- Simple and user-friendly interface to input text.
- Backend service that processes the input and calculates the number of words.
- Two execution options: using Docker Compose or running the backend and frontend separately.

---

## Prerequisites

Before running the project, ensure the following dependencies are installed on your machine:

- **Python 3.10 or later**
- **npm (Node Package Manager)** (latest version recommended)
- **Docker** and **Docker Compose** (if using the Docker option)

---

## Quick Start with Docker Compose

The easiest way to get the project running is by using Docker Compose. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rafaelandrade/voxy-count-words.git
   cd voxy-count-words

2. Start the application using Docker Compose

```bash
  docker-compose up --build
```

3. Access the application:

- Front-end: http:localhost:3000
- Back-end: http:localhost:8000

---

## Running Frontend and Backend Separately

### Backend

1. Navigate to the backend directory
```bash 
 cd backend
```

2. Install Python dependencies:
```bash 
 pip install -r requirements.txt 
```

3. Run the FastAPI server:
```
uvicorn app.main:app --reload --port 8000
```

4. The backend is now running at http:localhost:8000

### Frontend

1. Navigate to the frontend directory
```bash 
 cd frontend
```

2. Install Node dependencies:
```bash 
 npm install
```

3. Run the React development server:
```
npm run start
```

4. The frontend is now running at http:localhost:3000

---

### Notes

- Make sure to install all dependencies (npm install for the frontend and pip install for the backend) before running the project separately.
- For the best experience, use the latest versions of Python and NPM.

