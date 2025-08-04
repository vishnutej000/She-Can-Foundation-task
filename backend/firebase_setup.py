"""
Firebase setup script for initializing dummy data
Run this script to populate Firebase with initial user data
"""

import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    """Initialize Firebase with service account"""
    try:
        # For development, create a service account key file
        # In production, use proper service account credentials
        service_account_info = {
            "type": "service_account",
            "project_id": os.getenv('FIREBASE_PROJECT_ID'),
            "private_key_id": "dummy_key_id",
            "private_key": "-----BEGIN PRIVATE KEY-----\nDUMMY_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
            "client_email": f"firebase-adminsdk@{os.getenv('FIREBASE_PROJECT_ID')}.iam.gserviceaccount.com",
            "client_id": "dummy_client_id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
        
        if not firebase_admin._apps:
            cred = credentials.Certificate(service_account_info)
            firebase_admin.initialize_app(cred)
        
        return firestore.client()
    except Exception as e:
        print(f"Firebase initialization failed: {e}")
        return None

def populate_dummy_data():
    """Populate Firebase with dummy user data"""
    db = initialize_firebase()
    
    if not db:
        print("Could not initialize Firebase. Using mock data instead.")
        return
    
    dummy_users = [
        {
            "email": "john@example.com",
            "firstName": "John",
            "lastName": "Doe",
            "password": "password123",
            "donationsRaised": 2450.75,
            "referralCode": "johndoe2025",
            "createdAt": "2025-01-01T00:00:00Z"
        },
        {
            "email": "jane@example.com",
            "firstName": "Jane",
            "lastName": "Smith",
            "password": "password123",
            "donationsRaised": 1850.50,
            "referralCode": "janesmith2025",
            "createdAt": "2025-01-01T00:00:00Z"
        },
        {
            "email": "alice@example.com",
            "firstName": "Alice",
            "lastName": "Johnson",
            "password": "password123",
            "donationsRaised": 3200.25,
            "referralCode": "alicejohnson2025",
            "createdAt": "2025-01-01T00:00:00Z"
        }
    ]
    
    try:
        users_ref = db.collection('users')
        
        for user_data in dummy_users:
            # Check if user already exists
            query = users_ref.where('email', '==', user_data['email']).limit(1)
            existing = list(query.stream())
            
            if not existing:
                users_ref.add(user_data)
                print(f"Added user: {user_data['email']}")
            else:
                print(f"User already exists: {user_data['email']}")
        
        print("Dummy data population completed!")
        
    except Exception as e:
        print(f"Error populating data: {e}")

if __name__ == "__main__":
    populate_dummy_data()