import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

const HeroSection = () => {
  const navigate = useNavigate();

  return (
    <div className="text-center py-12">
      {/* Latest Tag */}
      <div className="inline-block px-3 py-1 mb-6 rounded-full text-sm bg-purple-800 text-purple-300">
        <span className="uppercase font-bold text-xs mr-2">New</span> Latest
        integration just arrived
      </div>

      {/* Title */}
      <h1 className="text-4xl font-bold text-white mb-4">
        Boost your <span className="text-purple-400">video production</span>{" "}
        with AI.
      </h1>

      {/* Subtitle */}
      <p className="text-gray-400 mb-8 text-lg">
        Create studio-quality videos with AI avatars in multiple languages. It's
        as easy as making a slide deck.
      </p>

      {/* Buttons */}
      <div className="flex justify-center space-x-4">
        <button
          onClick={() => navigate("/auth")}
          className="px-6 py-2 rounded-full bg-white text-black text-sm font-semibold hover:bg-gray-200 focus:ring focus:ring-gray-300"
        >
          Tutorial
        </button>
        <button
          onClick={() => navigate("/auth")}
          className="px-6 py-2 rounded-full bg-purple-600 text-white text-sm font-semibold hover:bg-purple-700 focus:ring focus:ring-purple-500"
        >
          Start Now
        </button>
      </div>
    </div>
  );
};

const VideoSection = () => {
  return (
    <div className="relative mt-12 flex justify-center">
      {/* Video Frame */}
      <div className="bg-black border border-gray-800 rounded-lg overflow-hidden w-4/5 md:w-3/5 p-4">
        <img
          src="https://media3.giphy.com/media/5zvSGqPcGvxIh473U3/giphy.gif?cid=6c09b952j3ccd78sfsshadnazbx0kvlpuedun5wsfmmqw49l&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"
          alt="Video Thumbnail"
          className="w-full h-auto rounded-md"
        />
      </div>
    </div>
  );
};

const LandingPage = () => {
  return (
    <div className="bg-black text-white">
      <Navbar />
      <HeroSection />
      <VideoSection />
    </div>
  );
};

export default LandingPage;
