# She Can Foundation - Intern Dashboard

A full-stack web application for managing intern fundraising activities with a dashboard, leaderboard, and authentication system.

## 🚀 Features

### Frontend (React + Vite + Tailwind CSS)
- ✅ **Dummy login/signup page** (no real auth needed)
- ✅ **Dashboard showing:**
  - Intern name
  - Dummy referral code (e.g., yourname2025)
  - Total donations raised (from backend)
  - Rewards/unlockables section (static display)
- ✅ **Bonus: Leaderboard page** with rankings and statistics

### Backend (Flask + Firebase)
- ✅ **REST API** with endpoints for:
  - User authentication (signin/signup)
  - User data management
  - Donations tracking
  - Leaderboard functionality
- ✅ **Firebase integration** (with fallback to mock data)
- ✅ **Environment variable configuration**

## 📁 Project Structure

```
She-Can-Foundation-task/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── SignIn.jsx
│   │   │   ├── SignUp.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── Leaderboard.jsx
│   │   ├── services/        # API services
│   │   │   └── api.js
│   │   └── App.jsx
│   ├── package.json
│   └── ...
├── backend/                  # Flask backend
│   ├── venv/                # Python virtual environment
│   ├── app.py               # Main Flask application
│   ├── run.py               # Development server runner
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment variables
│   └── ...
├── start_dev.bat            # Development startup script
└── README.md
```

## 🛠️ Quick Start

### Option 1: Use the Startup Script (Windows)
```bash
# Double-click or run from command line
start_dev.bat
```

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend

# Activate virtual environment
venv\Scripts\activate

# Install dependencies (already done)
pip install -r requirements.txt

# Start the Flask server
python run.py
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies (already done)
npm install

# Start the development server
npm run dev
```

## 🌐 Access the Application

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5000
- **API Health Check:** http://localhost:5000/api/health

## 👤 Test Users

Use these credentials to test the application:

1. **John Doe**
   - Email: `john@example.com`
   - Password: `password123`
   - Donations: $2,450.75

2. **Jane Smith**
   - Email: `jane@example.com`
   - Password: `password123`
   - Donations: $1,850.50

3. **Alice Johnson**
   - Email: `alice@example.com`
   - Password: `password123`
   - Donations: $3,200.25

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/signin` - User sign in
- `POST /api/auth/signup` - User registration

### User Management
- `GET /api/user/donations/<email>` - Get user donation data
- `PUT /api/user/donations/<email>` - Update user donations
- `GET /api/users` - Get all users

### Leaderboard
- `GET /api/leaderboard` - Get leaderboard rankings

### Health Check
- `GET /api/health` - API health status

## 🧪 Testing the API

Run the test script to verify all endpoints:

```bash
cd backend
venv\Scripts\activate
python test_api.py
```

## 🔥 Firebase Configuration

The application is configured to work with Firebase, but includes fallback mock data for development. Firebase credentials are stored in the `.env` file.

For production deployment, replace the dummy Firebase credentials with real service account keys.

## 🎯 Key Features Implemented

### ✅ Required Features
- [x] Dummy login/signup page (no auth needed)
- [x] Dashboard showing intern name
- [x] Dummy referral code generation
- [x] Total donations raised from backend
- [x] Rewards/unlockables section (static display)
- [x] Simple REST API returning dummy data
- [x] Backend can be tested with Postman

### ✅ Bonus Features
- [x] Leaderboard page with rankings
- [x] Data stored in Firebase (with mock fallback)
- [x] Full CRUD operations for user data
- [x] Responsive design with Tailwind CSS
- [x] Environment variable configuration
- [x] Comprehensive API testing

## 🚀 Technologies Used

### Frontend
- React 19.1.0
- Vite 7.0.4
- Tailwind CSS 3.4.13
- Axios for API calls

### Backend
- Flask 2.3.3
- Firebase Admin SDK 6.2.0
- Flask-CORS for cross-origin requests
- Python-dotenv for environment variables

## 📝 Development Notes

- The application uses a Python virtual environment for backend dependencies
- Frontend uses modern React with hooks and functional components
- Tailwind CSS provides responsive, utility-first styling
- Firebase integration includes proper error handling and fallbacks
- All API endpoints include proper error handling and validation

## 🎨 UI/UX Features

- Clean, professional design
- Responsive layout for mobile and desktop
- Interactive leaderboard with podium display
- Progress bars for rewards tracking
- Loading states and error handling
- Intuitive navigation between views

This project demonstrates a complete full-stack application with modern web development practices and technologies.