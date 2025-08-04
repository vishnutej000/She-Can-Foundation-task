from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, origins=[os.getenv('FRONTEND_URL', 'http://localhost:5173')])

# Initialize Firebase Admin SDK
# For development, we'll use a service account key
# In production, you should use proper service account credentials
try:
    # Initialize Firebase with default credentials (for development)
    if not firebase_admin._apps:
        # Create a dummy service account for development
        # In production, replace this with actual service account key
        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": os.getenv('FIREBASE_PROJECT_ID'),
            "private_key_id": "dummy_key_id",
            "private_key": "-----BEGIN PRIVATE KEY-----\nDUMMY_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
            "client_email": f"firebase-adminsdk@{os.getenv('FIREBASE_PROJECT_ID')}.iam.gserviceaccount.com",
            "client_id": "dummy_client_id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        })
        firebase_admin.initialize_app(cred)
    
    db = firestore.client()
    firebase_initialized = True
except Exception as e:
    print(f"Firebase initialization failed: {e}")
    print("Running in mock mode without Firebase")
    firebase_initialized = False
    db = None

# Mock data for when Firebase is not available
mock_users = {
    "john@example.com": {
        "email": "john@example.com",
        "firstName": "John",
        "lastName": "Doe",
        "password": "password123",
        "donationsRaised": 2450.75,
        "referralCode": "johndoe2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Marketing",
        "joinDate": "2024-12-01",
        "totalReferrals": 15
    },
    "jane@example.com": {
        "email": "jane@example.com",
        "firstName": "Jane",
        "lastName": "Smith",
        "password": "password123",
        "donationsRaised": 1850.50,
        "referralCode": "janesmith2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Communications",
        "joinDate": "2024-11-15",
        "totalReferrals": 12
    },
    "alice@example.com": {
        "email": "alice@example.com",
        "firstName": "Alice",
        "lastName": "Johnson",
        "password": "password123",
        "donationsRaised": 3200.25,
        "referralCode": "alicejohnson2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Outreach",
        "joinDate": "2024-10-20",
        "totalReferrals": 22
    },
    "bob@example.com": {
        "email": "bob@example.com",
        "firstName": "Bob",
        "lastName": "Wilson",
        "password": "password123",
        "donationsRaised": 1200.00,
        "referralCode": "bobwilson2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Social Media",
        "joinDate": "2024-12-10",
        "totalReferrals": 8
    },
    "sarah@example.com": {
        "email": "sarah@example.com",
        "firstName": "Sarah",
        "lastName": "Davis",
        "password": "password123",
        "donationsRaised": 4100.80,
        "referralCode": "sarahdavis2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Fundraising",
        "joinDate": "2024-09-05",
        "totalReferrals": 28
    },
    "mike@example.com": {
        "email": "mike@example.com",
        "firstName": "Mike",
        "lastName": "Brown",
        "password": "password123",
        "donationsRaised": 950.25,
        "referralCode": "mikebrown2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Events",
        "joinDate": "2024-12-20",
        "totalReferrals": 6
    },
    "emma@example.com": {
        "email": "emma@example.com",
        "firstName": "Emma",
        "lastName": "Garcia",
        "password": "password123",
        "donationsRaised": 2850.90,
        "referralCode": "emmagarcia2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Community Relations",
        "joinDate": "2024-11-01",
        "totalReferrals": 18
    },
    "david@example.com": {
        "email": "david@example.com",
        "firstName": "David",
        "lastName": "Martinez",
        "password": "password123",
        "donationsRaised": 1675.40,
        "referralCode": "davidmartinez2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Digital Marketing",
        "joinDate": "2024-11-25",
        "totalReferrals": 11
    },
    "lisa@example.com": {
        "email": "lisa@example.com",
        "firstName": "Lisa",
        "lastName": "Anderson",
        "password": "password123",
        "donationsRaised": 3750.60,
        "referralCode": "lisaanderson2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Partnership Development",
        "joinDate": "2024-10-10",
        "totalReferrals": 25
    },
    "chris@example.com": {
        "email": "chris@example.com",
        "firstName": "Chris",
        "lastName": "Taylor",
        "password": "password123",
        "donationsRaised": 2100.15,
        "referralCode": "christaylor2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Content Creation",
        "joinDate": "2024-11-30",
        "totalReferrals": 14
    },
    "maria@example.com": {
        "email": "maria@example.com",
        "firstName": "Maria",
        "lastName": "Rodriguez",
        "password": "password123",
        "donationsRaised": 1425.75,
        "referralCode": "mariarodriguez2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Volunteer Coordination",
        "joinDate": "2024-12-05",
        "totalReferrals": 9
    },
    "alex@example.com": {
        "email": "alex@example.com",
        "firstName": "Alex",
        "lastName": "Thompson",
        "password": "password123",
        "donationsRaised": 5200.30,
        "referralCode": "alexthompson2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Strategic Partnerships",
        "joinDate": "2024-08-15",
        "totalReferrals": 35
    },
    "sophie@example.com": {
        "email": "sophie@example.com",
        "firstName": "Sophie",
        "lastName": "White",
        "password": "password123",
        "donationsRaised": 875.50,
        "referralCode": "sophiewhite2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Research",
        "joinDate": "2024-12-15",
        "totalReferrals": 5
    },
    "ryan@example.com": {
        "email": "ryan@example.com",
        "firstName": "Ryan",
        "lastName": "Lee",
        "password": "password123",
        "donationsRaised": 3450.85,
        "referralCode": "ryanlee2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Corporate Relations",
        "joinDate": "2024-09-20",
        "totalReferrals": 23
    },
    "nina@example.com": {
        "email": "nina@example.com",
        "firstName": "Nina",
        "lastName": "Patel",
        "password": "password123",
        "donationsRaised": 1950.20,
        "referralCode": "ninapatel2025",
        "createdAt": "2025-01-01T00:00:00Z",
        "department": "Program Development",
        "joinDate": "2024-11-10",
        "totalReferrals": 13
    }
}

def get_user_by_email(email):
    """Get user data by email from Firebase or mock data"""
    if firebase_initialized and db:
        try:
            users_ref = db.collection('users')
            query = users_ref.where('email', '==', email).limit(1)
            docs = query.stream()
            
            for doc in docs:
                return doc.to_dict()
            return None
        except Exception as e:
            print(f"Firebase query failed: {e}")
            return mock_users.get(email)
    else:
        return mock_users.get(email)

def create_user(user_data):
    """Create a new user in Firebase or mock data"""
    if firebase_initialized and db:
        try:
            users_ref = db.collection('users')
            users_ref.add(user_data)
            return True
        except Exception as e:
            print(f"Firebase create failed: {e}")
            mock_users[user_data['email']] = user_data
            return True
    else:
        mock_users[user_data['email']] = user_data
        return True

def update_user_donations(email, amount):
    """Update user donations in Firebase or mock data"""
    if firebase_initialized and db:
        try:
            users_ref = db.collection('users')
            query = users_ref.where('email', '==', email).limit(1)
            docs = query.stream()
            
            for doc in docs:
                doc.reference.update({'donationsRaised': amount})
                return True
            return False
        except Exception as e:
            print(f"Firebase update failed: {e}")
            if email in mock_users:
                mock_users[email]['donationsRaised'] = amount
                return True
            return False
    else:
        if email in mock_users:
            mock_users[email]['donationsRaised'] = amount
            return True
        return False

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'firebase_connected': firebase_initialized,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/auth/signin', methods=['POST'])
def signin():
    """Sign in endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        user = get_user_by_email(email)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # In a real app, you'd hash and compare passwords
        if user.get('password') != password:
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Remove password from response
        user_response = {k: v for k, v in user.items() if k != 'password'}
        
        return jsonify({
            'message': 'Sign in successful',
            'user': user_response
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """Sign up endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        
        if not all([email, password, first_name, last_name]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Check if user already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            return jsonify({'error': 'User already exists'}), 409
        
        # Generate referral code
        referral_code = f"{first_name.lower()}{last_name.lower()}2025"
        
        # Create new user
        new_user = {
            'email': email,
            'password': password,  # In real app, hash this
            'firstName': first_name,
            'lastName': last_name,
            'donationsRaised': 0.0,
            'referralCode': referral_code,
            'createdAt': datetime.now().isoformat()
        }
        
        success = create_user(new_user)
        
        if success:
            # Remove password from response
            user_response = {k: v for k, v in new_user.items() if k != 'password'}
            return jsonify({
                'message': 'User created successfully',
                'user': user_response
            }), 201
        else:
            return jsonify({'error': 'Failed to create user'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/donations/<email>', methods=['GET'])
def get_user_donations(email):
    """Get user donations"""
    try:
        user = get_user_by_email(email)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'donationsRaised': user.get('donationsRaised', 0.0),
            'referralCode': user.get('referralCode', ''),
            'email': email
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/donations/<email>', methods=['PUT'])
def update_donations(email):
    """Update user donations"""
    try:
        data = request.get_json()
        amount = data.get('amount')
        
        if amount is None:
            return jsonify({'error': 'Amount is required'}), 400
        
        success = update_user_donations(email, float(amount))
        
        if success:
            return jsonify({
                'message': 'Donations updated successfully',
                'donationsRaised': float(amount)
            }), 200
        else:
            return jsonify({'error': 'Failed to update donations'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users (for admin/testing purposes)"""
    try:
        if firebase_initialized and db:
            users_ref = db.collection('users')
            docs = users_ref.stream()
            users = []
            for doc in docs:
                user_data = doc.to_dict()
                # Remove passwords from response
                user_data.pop('password', None)
                users.append(user_data)
            return jsonify({'users': users}), 200
        else:
            # Return mock users without passwords
            users = []
            for user in mock_users.values():
                user_copy = user.copy()
                user_copy.pop('password', None)
                users.append(user_copy)
            return jsonify({'users': users}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get leaderboard data sorted by donations raised"""
    try:
        if firebase_initialized and db:
            users_ref = db.collection('users')
            docs = users_ref.stream()
            users = []
            for doc in docs:
                user_data = doc.to_dict()
                # Remove passwords from response
                user_data.pop('password', None)
                users.append(user_data)
        else:
            # Use mock users without passwords
            users = []
            for user in mock_users.values():
                user_copy = user.copy()
                user_copy.pop('password', None)
                users.append(user_copy)
        
        # Sort by donations raised (descending)
        leaderboard = sorted(users, key=lambda x: x.get('donationsRaised', 0), reverse=True)
        
        # Add rank to each user
        for i, user in enumerate(leaderboard):
            user['rank'] = i + 1
        
        return jsonify({'leaderboard': leaderboard}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get overall statistics"""
    try:
        if firebase_initialized and db:
            users_ref = db.collection('users')
            docs = users_ref.stream()
            users = [doc.to_dict() for doc in docs]
        else:
            users = list(mock_users.values())
        
        total_users = len(users)
        total_donations = sum(user.get('donationsRaised', 0) for user in users)
        total_referrals = sum(user.get('totalReferrals', 0) for user in users)
        avg_donation = total_donations / total_users if total_users > 0 else 0
        
        # Department breakdown
        departments = {}
        for user in users:
            dept = user.get('department', 'Unknown')
            if dept not in departments:
                departments[dept] = {'count': 0, 'donations': 0}
            departments[dept]['count'] += 1
            departments[dept]['donations'] += user.get('donationsRaised', 0)
        
        return jsonify({
            'totalUsers': total_users,
            'totalDonations': round(total_donations, 2),
            'totalReferrals': total_referrals,
            'averageDonation': round(avg_donation, 2),
            'departments': departments
        }), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    """Get rewards/achievements data"""
    try:
        rewards_data = [
            {
                "id": 1,
                "title": "First Steps",
                "description": "Raise your first $50",
                "target": 50,
                "icon": "🌱",
                "category": "Beginner"
            },
            {
                "id": 2,
                "title": "Bronze Supporter",
                "description": "Raise $100 in donations",
                "target": 100,
                "icon": "🥉",
                "category": "Bronze"
            },
            {
                "id": 3,
                "title": "Community Builder",
                "description": "Get 5 referrals",
                "target": 5,
                "icon": "👥",
                "category": "Social",
                "type": "referrals"
            },
            {
                "id": 4,
                "title": "Silver Champion",
                "description": "Raise $500 in donations",
                "target": 500,
                "icon": "🥈",
                "category": "Silver"
            },
            {
                "id": 5,
                "title": "Network Master",
                "description": "Get 10 referrals",
                "target": 10,
                "icon": "🌐",
                "category": "Social",
                "type": "referrals"
            },
            {
                "id": 6,
                "title": "Gold Ambassador",
                "description": "Raise $1000 in donations",
                "target": 1000,
                "icon": "🥇",
                "category": "Gold"
            },
            {
                "id": 7,
                "title": "Super Connector",
                "description": "Get 20 referrals",
                "target": 20,
                "icon": "⭐",
                "category": "Social",
                "type": "referrals"
            },
            {
                "id": 8,
                "title": "Platinum Leader",
                "description": "Raise $2500 in donations",
                "target": 2500,
                "icon": "💎",
                "category": "Platinum"
            },
            {
                "id": 9,
                "title": "Influence Master",
                "description": "Get 30 referrals",
                "target": 30,
                "icon": "🚀",
                "category": "Social",
                "type": "referrals"
            },
            {
                "id": 10,
                "title": "Diamond Elite",
                "description": "Raise $5000 in donations",
                "target": 5000,
                "icon": "💍",
                "category": "Diamond"
            }
        ]
        
        return jsonify({'rewards': rewards_data}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recent-activities', methods=['GET'])
def get_recent_activities():
    """Get recent activities/donations"""
    try:
        # Mock recent activities data
        activities = [
            {
                "id": 1,
                "type": "donation",
                "user": "Sarah Davis",
                "amount": 150.00,
                "timestamp": "2025-01-08T14:30:00Z",
                "description": "Corporate sponsorship secured"
            },
            {
                "id": 2,
                "type": "referral",
                "user": "Alex Thompson",
                "referralName": "Jennifer Wilson",
                "timestamp": "2025-01-08T13:15:00Z",
                "description": "New volunteer referred"
            },
            {
                "id": 3,
                "type": "donation",
                "user": "Lisa Anderson",
                "amount": 75.50,
                "timestamp": "2025-01-08T12:45:00Z",
                "description": "Community fundraiser event"
            },
            {
                "id": 4,
                "type": "achievement",
                "user": "Emma Garcia",
                "achievement": "Gold Ambassador",
                "timestamp": "2025-01-08T11:20:00Z",
                "description": "Reached $1000 milestone"
            },
            {
                "id": 5,
                "type": "donation",
                "user": "Ryan Lee",
                "amount": 200.00,
                "timestamp": "2025-01-08T10:30:00Z",
                "description": "Monthly donor program"
            },
            {
                "id": 6,
                "type": "referral",
                "user": "Alice Johnson",
                "referralName": "Michael Chen",
                "timestamp": "2025-01-08T09:15:00Z",
                "description": "Professional network referral"
            },
            {
                "id": 7,
                "type": "donation",
                "user": "Chris Taylor",
                "amount": 125.25,
                "timestamp": "2025-01-08T08:45:00Z",
                "description": "Social media campaign success"
            },
            {
                "id": 8,
                "type": "achievement",
                "user": "David Martinez",
                "achievement": "Silver Champion",
                "timestamp": "2025-01-07T16:30:00Z",
                "description": "Reached $500 milestone"
            }
        ]
        
        return jsonify({'activities': activities}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')