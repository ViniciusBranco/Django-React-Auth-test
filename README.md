# Django+React: A Note Taken Authenticated Test-App

A full-stack note-taking application built with Django REST Framework and React.

## Features

- User authentication with JWT
- Create, read, and delete notes (To be implemented)
- Protected routes
- Automatic token refresh
- Dockerized services (PostgreSQL, Django, React)

## Tech Stack

### Backend
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL

### Frontend
- React
- React Router
- Axios
- JWT Decode

## Setup

### Using Docker (Recommended)

1. Create `.env` file in the root directory based on `.env.example`:
```bash
DB_NAME=bkndb
DB_USER=bkndb
DB_PASSWORD=your_secure_password
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

2. Start the services:
```bash
docker-compose --env-file .env up
```

3. Access the application:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

### Manual Setup (Development)

#### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

### Required Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| DB_NAME | PostgreSQL database name | bkndb |
| DB_USER | PostgreSQL username | bkndb |
| DB_PASSWORD | PostgreSQL password | bkndb |
| DEBUG | Django debug mode | 1 |
| DJANGO_ALLOWED_HOSTS | Allowed hosts for Django | localhost,127.0.0.1 |
| CORS_ALLOWED_ORIGINS | CORS allowed origins | http://localhost:5173 |

### Frontend (.env)
```
VITE_API_URL="http://localhost:8000"
```

## API Endpoints

- `POST /api/user/register/` - Register new user
- `POST /api/token/` - Get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `GET /api/notes/` - List user's notes
- `POST /api/notes/` - Create new note
- `DELETE /api/notes/delete/<id>` - Delete note

## Docker Commands

```bash
# Build and start containers
docker-compose --env-file .env up

# Build containers without cache
docker-compose build --no-cache

# Stop containers
docker-compose down

# Stop containers and remove volumes
docker-compose down -v

# View logs
docker-compose logs -f
```
