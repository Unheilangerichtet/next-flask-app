## Overview

This is a full-stack web application that combines **Next.js** for the frontend, **Flask** for the backend API, **PostgreSQL** for database management, and **DaisyUI** for UI components. **Docker** is used to containerize the application, ensuring a consistent environment across all development stages

## Project Structure

```bash
├── .gitignore               # Git ignore rules
├── docker-compose.yml       # Docker Compose configuration
├── README.md                # Project documentation
├── client/                  # Frontend (Next.js)
│   ├── public/              # Public assets (images, icons)
│   ├── src/                 # Source code (pages, components)
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   ├── postcss.config.js    # PostCSS configuration
│   └── package.json         # Frontend dependencies and scripts
├── server/                  # Backend (Flask)
│   ├── app.py               # Main Flask app
│   ├── db.py                # Database connection setup
│   ├── routes/              # API routes
│   ├── services/            # Business logic
│   ├── .env                 # Environment variables (e.g., DB credentials)
│   ├── Dockerfile           # Dockerfile for Flask app
│   └── requirements.txt     # Backend dependencies
└── docker-compose.yml       # Docker Compose configuration
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Unheilangerichtet/next-flask-app
cd your-repo
```

### 2. Install Dependencies

```bash
cd client
npm install
```

```bash
cd server
pip install -r requirements.txt
```

### 3. Environment Variables

In the `server/` directory, create a `.env` file for the Flask backend with the following:

```env
DB_URI=postgresql://postgres:password@db/mydatabase
```

### 4. Run the Application with Docker Compose

```bash
docker-compose up --build
```

### 5. Access the Application

- **Frontend (Next.js)**: `http://localhost:3000`.
- **Backend (Flask)**: `http://localhost:5000`.
