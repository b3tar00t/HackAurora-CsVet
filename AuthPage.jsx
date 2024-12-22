import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add actual authentication logic here
    navigate("/dashboard");
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-br from-black via-gray-900 to-purple-900">
      {/* Glowing Box */}
      <div className="relative w-full max-w-lg p-10 bg-gray-900 bg-opacity-90 rounded-2xl shadow-xl backdrop-blur-md border-2 border-purple-600">
        {/* Glowing Effect */}
        <div className="absolute -inset-1 -z-10 rounded-2xl bg-purple-500 opacity-10 blur-3xl"></div>
        <div className="absolute -inset-4 -z-20 rounded-2xl bg-purple-700 opacity-30 blur-[100px]"></div>

        {/* Title */}
        <h1 className="text-4xl font-bold text-purple-300 text-center mb-8">
          {isLogin ? "Login" : "Sign Up"}
        </h1>

        {/* Form */}
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            className="w-full p-4 mb-6 border border-gray-700 rounded-lg bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-4 mb-6 border border-gray-700 rounded-lg bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
          <button
            type="submit"
            className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-4 rounded-lg text-lg transition-all duration-200"
          >
            {isLogin ? "Login" : "Sign Up"}
          </button>
        </form>

        {/* Toggle Button */}
        <button
          className="w-full mt-6 text-purple-400 hover:text-purple-300 font-medium text-center text-lg"
          onClick={() => setIsLogin(!isLogin)}
        >
          {isLogin
            ? "Don't have an account? Create one"
            : "Already have an account? Login"}
        </button>
      </div>
    </div>
  );
};

export default AuthPage;
