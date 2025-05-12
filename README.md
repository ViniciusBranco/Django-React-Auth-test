# Vita.AI Note Taking App

A full-stack note-taking application built with Django REST Framework and React.

## Features

- User authentication with JWT
- Create, read, and delete notes
- Protected routes
- Automatic token refresh

## Tech Stack

### Backend
- Django
- Django REST Framework
- Simple JWT
- SQLite3

### Frontend
- React
- React Router
- Axios
- JWT Decode

## Setup

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

### Frontend (.env)
```
VITE_API_URL="http://127.0.0.1:8000"
```

## API Endpoints

- `POST /api/user/register/` - Register new user
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `GET /api/notes/` - List user's notes
- `POST /api/notes/` - Create new note
- `DELETE /api/notes/delete/<id>` - Delete note