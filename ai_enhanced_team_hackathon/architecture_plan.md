# Architecture Plan

## Overview
The AI Decision Helper follows a three-tier architecture: React frontend, FastAPI backend, and PostgreSQL database.

## High-Level System Diagram

    +------------------+
    |   User Browser   |
    +------------------+
             |
             | HTTPS
             v
    +------------------+
    |    Frontend      |
    |  React+Tailwind  |
    |    (Vercel)      |
    +------------------+
             |
             | REST API (JSON)
             v
    +------------------+
    |   Backend API    |
    |    FastAPI       |
    |    (Render)      |
    +------------------+
             |
             | SQL
             v
    +------------------+
    |    Database      |
    |   PostgreSQL     |
    |   (Supabase)     |
    +------------------+

## Components

### Frontend
- Built with React and Tailwind CSS
- Handles user input, displays AI-generated pros and cons
- Communicates with backend via REST API
- Deployed on Vercel

### Backend API
- Built with FastAPI (Python)
- Handles authentication, decision CRUD, and AI integration
- Calls OpenAI API to generate pros and cons
- Deployed on Render

### Database
- PostgreSQL hosted on Supabase
- Stores users, decisions, and arguments

## Data Flow
1. User submits a decision description via the React frontend
2. Frontend sends a POST request to the FastAPI backend
3. Backend calls the OpenAI API to generate pros and cons
4. Results are saved to PostgreSQL and returned to the frontend
5. User reviews, edits, votes, and saves the final decision
