import { useState } from 'react';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Dashboard from './components/Dashboard';
import Leaderboard from './components/Leaderboard';
import { authAPI } from './services/api';
import './App.css';

function App() {
  const [currentView, setCurrentView] = useState('signin'); // 'signin', 'signup', 'dashboard', 'leaderboard'
  const [user, setUser] = useState(null);

  const handleSignIn = async (formData) => {
    try {
      const response = await authAPI.signin(formData);
      setUser(response.user);
      setCurrentView('dashboard');
      console.log('Sign in successful:', response.message);
    } catch (error) {
      console.error('Sign in failed:', error);
      alert(error.error || 'Sign in failed. Please try again.');
    }
  };

  const handleSignUp = async (formData) => {
    try {
      const response = await authAPI.signup(formData);
      setUser(response.user);
      setCurrentView('dashboard');
      console.log('Sign up successful:', response.message);
    } catch (error) {
      console.error('Sign up failed:', error);
      alert(error.error || 'Sign up failed. Please try again.');
    }
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentView('signin');
  };

  const handleViewLeaderboard = () => {
    setCurrentView('leaderboard');
  };

  const handleBackToDashboard = () => {
    setCurrentView('dashboard');
  };

  // If user is logged in, show appropriate view
  if (user) {
    if (currentView === 'leaderboard') {
      return (
        <Leaderboard
          onBack={handleBackToDashboard}
          currentUser={user}
        />
      );
    }
    return (
      <Dashboard
        user={user}
        onLogout={handleLogout}
        onViewLeaderboard={handleViewLeaderboard}
      />
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
