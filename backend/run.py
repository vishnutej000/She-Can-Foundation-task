"""
Development server runner
"""

from app import app
import os

if __name__ == '__main__':
    # Run the Flask development server
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask server on port {port}")
    print(f"Debug mode: {debug}")
    print("Backend API will be available at: http://localhost:5000")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )