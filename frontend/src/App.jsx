import { useState } from 'react';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import './App.css';

function App() {
  const [currentView, setCurrentView] = useState('signin'); // 'signin' or 'signup'
  const [user, setUser] = useState(null);

  const handleSignIn = (formData) => {
    // Handle sign in logic here
    console.log('Sign in data:', formData);
    // For now, just simulate successful login
    setUser({ email: formData.email });
  };

  const handleSignUp = (formData) => {
    // Handle sign up logic here
    console.log('Sign up data:', formData);
    // For now, just simulate successful registration
    setUser({ email: formData.email, firstName: formData.firstName, lastName: formData.lastName });
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentView('signin');
  };

  // If user is logged in, show a simple dashboard
  if (user) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="max-w-md w-full bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Welcome!</h2>
          <p className="text-gray-600 mb-4">
            You are successfully logged in as: <strong>{user.email}</strong>
          </p>
          {user.firstName && (
            <p className="text-gray-600 mb-4">
              Name: <strong>{user.firstName} {user.lastName}</strong>
            </p>
          )}
          <button
            onClick={handleLogout}
            className="w-full bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-md"
          >
            Logout
          </button>
        </div>
      </div>
    );
  }

  // Show authentication forms
  if (currentView === 'signin') {
    return (
      <SignIn
        onSwitchToSignUp={() => setCurrentView('signup')}
        onSignIn={handleSignIn}
      />
    );
  }

  return (
    <SignUp
      onSwitchToSignIn={() => setCurrentView('signin')}
      onSignUp={handleSignUp}
    />
  );
}

export default App;
