"""
Simple script to test the Flask API endpoints
"""

import requests
import json

BASE_URL = 'http://localhost:5000/api'

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/health')
        print(f"Health Check: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_signin():
    """Test signin endpoint"""
    try:
        data = {
            "email": "john@example.com",
            "password": "password123"
        }
        response = requests.post(f'{BASE_URL}/auth/signin', json=data)
        print(f"\nSign In Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Sign in test failed: {e}")
        return False

def test_signup():
    """Test signup endpoint"""
    try:
        data = {
            "email": "test@example.com",
            "password": "password123",
            "firstName": "Test",
            "lastName": "User"
        }
        response = requests.post(f'{BASE_URL}/auth/signup', json=data)
        print(f"\nSign Up Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code in [200, 201, 409]  # 409 if user exists
    except Exception as e:
        print(f"Sign up test failed: {e}")
        return False

def test_get_donations():
    """Test get donations endpoint"""
    try:
        email = "john@example.com"
        response = requests.get(f'{BASE_URL}/user/donations/{email}')
        print(f"\nGet Donations Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get donations test failed: {e}")
        return False

def test_get_users():
    """Test get all users endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/users')
        print(f"\nGet Users Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get users test failed: {e}")
        return False

def test_get_leaderboard():
    """Test get leaderboard endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/leaderboard')
        print(f"\nGet Leaderboard Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get leaderboard test failed: {e}")
        return False

def test_get_stats():
    """Test get stats endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/stats')
        print(f"\nGet Stats Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get stats test failed: {e}")
        return False

def test_get_rewards():
    """Test get rewards endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/rewards')
        print(f"\nGet Rewards Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get rewards test failed: {e}")
        return False

def test_get_activities():
    """Test get recent activities endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/recent-activities')
        print(f"\nGet Recent Activities Test: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"Get recent activities test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Flask API Endpoints")
    print("=" * 40)
    
    tests = [
        ("Health Check", test_health),
        ("Sign In", test_signin),
        ("Sign Up", test_signup),
        ("Get Donations", test_get_donations),
        ("Get Users", test_get_users),
        ("Get Leaderboard", test_get_leaderboard),
        ("Get Stats", test_get_stats),
        ("Get Rewards", test_get_rewards),
        ("Get Recent Activities", test_get_activities),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        success = test_func()
        results.append((test_name, success))
    
    print(f"\n{'='*40}")
    print("Test Results:")
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name}: {status}")

if __name__ == "__main__":
    main()