import { useState, useEffect } from 'react';
import { userAPI } from '../services/api';

const Dashboard = ({ user, onLogout, onViewLeaderboard }) => {
  const [donationsRaised, setDonationsRaised] = useState(0);
  const [loading, setLoading] = useState(true);

  // Generate referral code based on user name
  const generateReferralCode = (firstName, lastName) => {
    const name = firstName && lastName ? `${firstName}${lastName}` : 'intern';
    return `${name.toLowerCase()}2025`;
  };

  // Fetch donations from backend
  useEffect(() => {
    const fetchDonations = async () => {
      setLoading(true);
      try {
        const response = await userAPI.getDonations(user.email);
        setDonationsRaised(response.donationsRaised);
      } catch (error) {
        console.error('Failed to fetch donations:', error);
        // Fallback to user data if API fails
        setDonationsRaised(user.donationsRaised || 0);
      } finally {
        setLoading(false);
      }
    };

    if (user?.email) {
      fetchDonations();
    }
  }, [user]);

  const referralCode = generateReferralCode(user.firstName, user.lastName);

  const [rewards, setRewards] = useState([]);
  const [recentActivities, setRecentActivities] = useState([]);
  const [stats, setStats] = useState(null);

  // Fetch rewards data
  useEffect(() => {
    const fetchRewards = async () => {
      try {
        const response = await userAPI.getRewards();
        const rewardsWithStatus = response.rewards.map(reward => ({
          ...reward,
          unlocked: reward.type === 'referrals' 
            ? (user.totalReferrals || 0) >= reward.target
            : donationsRaised >= reward.target
        }));
        setRewards(rewardsWithStatus);
      } catch (error) {
        console.error('Failed to fetch rewards:', error);
        // Fallback rewards
        setRewards([
          {
            id: 1,
            title: "Bronze Supporter",
            description: "Raise $100 in donations",
            target: 100,
            unlocked: donationsRaised >= 100,
            icon: "🥉",
            category: "Bronze"
          },
          {
            id: 2,
            title: "Silver Champion",
            description: "Raise $500 in donations",
            target: 500,
            unlocked: donationsRaised >= 500,
            icon: "🥈",
            category: "Silver"
          },
          {
            id: 3,
            title: "Gold Ambassador",
            description: "Raise $1000 in donations",
            target: 1000,
            unlocked: donationsRaised >= 1000,
            icon: "🥇",
            category: "Gold"
          },
          {
            id: 4,
            title: "Platinum Leader",
            description: "Raise $2500 in donations",
            target: 2500,
            unlocked: donationsRaised >= 2500,
            icon: "💎",
            category: "Platinum"
          },
          {
            id: 5,
            title: "Diamond Elite",
            description: "Raise $5000 in donations",
            target: 5000,
            unlocked: donationsRaised >= 5000,
            icon: "💍",
            category: "Diamond"
          }
        ]);
      }
    };

    const fetchRecentActivities = async () => {
      try {
        const response = await userAPI.getRecentActivities();
        setRecentActivities(response.activities.slice(0, 5)); // Show only 5 recent
      } catch (error) {
        console.error('Failed to fetch recent activities:', error);
      }
    };

    const fetchStats = async () => {
      try {
        const response = await userAPI.getStats();
        setStats(response);
      } catch (error) {
        console.error('Failed to fetch stats:', error);
      }
    };

    if (donationsRaised !== 0) {
      fetchRewards();
      fetchRecentActivities();
      fetchStats();
    }
  }, [donationsRaised, user]);

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">She Can Foundation</h1>
              <p className="text-sm text-gray-600">Intern Dashboard</p>
            </div>
            <button
              onClick={onLogout}
              className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-md text-sm font-medium"
            >
              Logout
            </button>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section */}
        <div className="bg-white rounded-lg shadow-sm p-6 mb-8">
          <div className="flex items-center space-x-4">
            <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center">
              <span className="text-2xl font-bold text-indigo-600">
                {user.firstName ? user.firstName.charAt(0) : 'I'}
              </span>
            </div>
            <div>
              <h2 className="text-2xl font-bold text-gray-900">
                Welcome, {user.firstName || 'Intern'} {user.lastName || ''}!
              </h2>
              <p className="text-gray-600">Keep up the great work raising funds for our cause</p>
            </div>
          </div>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 mb-8">
          {/* Referral Code */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-blue-100 rounded-md flex items-center justify-center">
                  <span className="text-blue-600 font-bold">#</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Your Referral Code</p>
                <p className="text-2xl font-bold text-gray-900">{referralCode}</p>
              </div>
            </div>
          </div>

          {/* Total Donations */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-green-100 rounded-md flex items-center justify-center">
                  <span className="text-green-600 font-bold">$</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Total Donations Raised</p>
                {loading ? (
                  <div className="animate-pulse">
                    <div className="h-8 bg-gray-200 rounded w-24"></div>
                  </div>
                ) : (
                  <p className="text-2xl font-bold text-gray-900">${donationsRaised.toFixed(2)}</p>
                )}
              </div>
            </div>
          </div>

          {/* Active Rewards */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-purple-100 rounded-md flex items-center justify-center">
                  <span className="text-purple-600 font-bold">🏆</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Rewards Unlocked</p>
                <p className="text-2xl font-bold text-gray-900">
                  {rewards.filter(r => r.unlocked).length}/{rewards.length}
                </p>
              </div>
            </div>
          </div>

          {/* Total Referrals */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-orange-100 rounded-md flex items-center justify-center">
                  <span className="text-orange-600 font-bold">👥</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Total Referrals</p>
                <p className="text-2xl font-bold text-gray-900">
                  {user.totalReferrals || 0}
                </p>
              </div>
            </div>
          </div>

          {/* Department */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-indigo-100 rounded-md flex items-center justify-center">
                  <span className="text-indigo-600 font-bold">🏢</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">Department</p>
                <p className="text-lg font-bold text-gray-900">
                  {user.department || 'General'}
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
          {/* Rewards Section */}
          <div className="lg:col-span-2 bg-white rounded-lg shadow-sm p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-6">Rewards & Achievements</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {rewards.slice(0, 6).map((reward) => {
                const currentValue = reward.type === 'referrals' ? (user.totalReferrals || 0) : donationsRaised;
                const progressPercent = Math.min((currentValue / reward.target) * 100, 100);
                
                return (
                  <div
                    key={reward.id}
                    className={`p-4 rounded-lg border-2 transition-all ${
                      reward.unlocked
                        ? 'border-green-200 bg-green-50'
                        : 'border-gray-200 bg-gray-50'
                    }`}
                  >
                    <div className="flex items-center space-x-3">
                      <span className={`text-2xl ${reward.unlocked ? 'grayscale-0' : 'grayscale'}`}>
                        {reward.icon}
                      </span>
                      <div className="flex-1">
                        <h4 className={`font-medium ${
                          reward.unlocked ? 'text-green-900' : 'text-gray-600'
                        }`}>
                          {reward.title}
                        </h4>
                        <p className={`text-sm ${
                          reward.unlocked ? 'text-green-700' : 'text-gray-500'
                        }`}>
                          {reward.description}
                        </p>
                        <div className="mt-2">
                          <div className="flex justify-between text-xs text-gray-600 mb-1">
                            <span>
                              {reward.type === 'referrals' ? currentValue : `$${currentValue.toFixed(0)}`}
                            </span>
                            <span>
                              {reward.type === 'referrals' ? reward.target : `$${reward.target}`}
                            </span>
                          </div>
                          <div className="w-full bg-gray-200 rounded-full h-2">
                            <div
                              className={`h-2 rounded-full transition-all ${
                                reward.unlocked ? 'bg-green-500' : 'bg-blue-500'
                              }`}
                              style={{ width: `${progressPercent}%` }}
                            ></div>
                          </div>
                        </div>
                      </div>
                    </div>
                    {reward.unlocked && (
                      <div className="mt-2 text-right">
                        <span className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                          ✓ Unlocked
                        </span>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Recent Activities */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-6">Recent Activities</h3>
            <div className="space-y-4">
              {recentActivities.length > 0 ? (
                recentActivities.map((activity) => (
                  <div key={activity.id} className="flex items-start space-x-3">
                    <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm ${
                      activity.type === 'donation' ? 'bg-green-100 text-green-600' :
                      activity.type === 'referral' ? 'bg-blue-100 text-blue-600' :
                      'bg-purple-100 text-purple-600'
                    }`}>
                      {activity.type === 'donation' ? '💰' :
                       activity.type === 'referral' ? '👥' : '🏆'}
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium text-gray-900">
                        {activity.user}
                      </p>
                      <p className="text-sm text-gray-600">
                        {activity.type === 'donation' && `Raised $${activity.amount}`}
                        {activity.type === 'referral' && `Referred ${activity.referralName}`}
                        {activity.type === 'achievement' && `Earned ${activity.achievement}`}
                      </p>
                      <p className="text-xs text-gray-400">
                        {new Date(activity.timestamp).toLocaleDateString()}
                      </p>
                    </div>
                  </div>
                ))
              ) : (
                <div className="text-center text-gray-500 py-8">
                  <div className="text-4xl mb-2">📊</div>
                  <p>No recent activities</p>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="mt-8 bg-white rounded-lg shadow-sm p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <button 
              onClick={onViewLeaderboard}
              className="p-4 text-left border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
            >
              <div className="text-indigo-600 text-xl mb-2">🏆</div>
              <h4 className="font-medium text-gray-900">View Leaderboard</h4>
              <p className="text-sm text-gray-600">See top fundraisers</p>
            </button>
            <button className="p-4 text-left border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <div className="text-indigo-600 text-xl mb-2">📊</div>
              <h4 className="font-medium text-gray-900">View Analytics</h4>
              <p className="text-sm text-gray-600">See detailed donation statistics</p>
            </button>
            <button className="p-4 text-left border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <div className="text-indigo-600 text-xl mb-2">📢</div>
              <h4 className="font-medium text-gray-900">Share Campaign</h4>
              <p className="text-sm text-gray-600">Share your referral code</p>
            </button>
            <button className="p-4 text-left border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <div className="text-indigo-600 text-xl mb-2">💬</div>
              <h4 className="font-medium text-gray-900">Get Support</h4>
              <p className="text-sm text-gray-600">Contact our team for help</p>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;