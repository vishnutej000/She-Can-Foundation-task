import React from "react";

export default function TailwindTestPage() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600">
      <div className="bg-white rounded-xl shadow-lg p-8 w-full max-w-md text-center">
        <h1 className="text-3xl font-bold text-blue-700 mb-4">Tailwind CSS Test Page</h1>
        <p className="text-gray-700 mb-6">If you see colors, rounded corners, and shadows, Tailwind CSS is working!</p>
        <button className="bg-purple-600 hover:bg-purple-800 text-white font-semibold py-2 px-6 rounded-lg shadow transition-all">Test Button</button>
        <div className="mt-8 grid grid-cols-3 gap-4">
          <div className="h-12 w-12 bg-blue-400 rounded-full"></div>
          <div className="h-12 w-12 bg-green-400 rounded-full"></div>
          <div className="h-12 w-12 bg-pink-400 rounded-full"></div>
        </div>
      </div>
    </div>
  );
}
