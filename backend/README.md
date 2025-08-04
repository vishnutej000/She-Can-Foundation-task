# She Can Foundation - Backend API

Flask backend with Firebase integration for the She Can Foundation intern dashboard.

## Setup Instructions

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Configuration

The `.env` file is already configured with Firebase credentials. For production, you should:

1. Create a proper Firebase service account key
2. Replace the dummy credentials in the code
3. Set up proper authentication

### 3. Firebase Setup (Optional)

To use real Firebase instead of mock data:

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: `she-can-foundation-c3dce`
3. Go to Project Settings > Service Accounts
4. Generate a new private key
5. Replace the dummy credentials in `app.py` with the real service account key

### 4. Run the Development Server

```bash
# Option 1: Direct run
python app.py

# Option 2: Using the run script
python run.py

# Option 3: Using Flask CLI
flask run
```

The API will be available at: `http://localhost:5000`

### 5. Populate Dummy Data (Optional)

```bash
python firebase_setup.py
```

## API Endpoints

### Authentication
- `POST /api/auth/signin` - User sign in
- `POST /api/auth/signup` - User registration

### User Management
- `GET /api/user/donations/<email>` - Get user donation data
- `PUT /api/user/donations/<email>` - Update user donations
- `GET /api/users` - Get all users (admin)

### Health Check
- `GET /api/health` - API health status

## Mock Users (for testing)

When Firebase is not available, the following mock users are available:

1. **John Doe**
   - Email: `john@example.com`
   - Password: `password123`
   - Donations: $2,450.75

2. **Jane Smith**
   - Email: `jane@example.com`
   - Password: `password123`
   - Donations: $1,850.50

## Environment Variables

- `FIREBASE_PROJECT_ID` - Firebase project ID
- `FIREBASE_API_KEY` - Firebase API key
- `FLASK_ENV` - Flask environment (development/production)
- `FLASK_DEBUG` - Enable debug mode
- `FRONTEND_URL` - Frontend URL for CORS

## Production Deployment

For production deployment:

1. Set up proper Firebase service account credentials
2. Use environment variables for sensitive data
3. Set `FLASK_ENV=production`
4. Use a production WSGI server like Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```