# System Architecture

## Overview
The Task Management MVP follows a three-tier architecture: frontend, backend API, and database.

## High-Level System Diagram
## Components

### Frontend
- Built with React and Tailwind CSS
- Communicates with backend via REST API
- Deployed on Vercel

### Backend API
- Built with FastAPI (Python)
- Handles authentication and task CRUD operations
- JWT-based authentication
- Deployed on Render

### Database
- PostgreSQL hosted on Supabase
- Stores users, tasks, and categories

## Data Flow
1. User interacts with the React frontend in the browser
2. Frontend sends HTTP requests to the FastAPI backend
3. Backend validates the request and queries PostgreSQL
4. Response is returned to the frontend and displayed to the user
