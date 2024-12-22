import React from "react";

const Navbar = () => {
  return (
    <nav className="flex items-center justify-between py-4 px-6 bg-black text-white">
      {/* Logo */}
      <div>
        <div className="w-6 h-6 rounded-full bg-purple-700 flex items-center justify-center">
          <div className="w-3 h-3 bg-purple-400 rounded-full"></div>
        </div>
      </div>

      {/* Nav Links */}
      <ul className="flex space-x-6 text-gray-300">
        <li className="group relative">
          <button className="hover:text-white">Features</button>
        </li>
        <li className="group relative">
          <button className="hover:text-white">Developers</button>
        </li>
        <li className="group relative">
          <button className="hover:text-white">Company</button>
        </li>
        <li className="group relative">
          <button className="hover:text-white">Blog</button>
        </li>
        <li className="group relative">
          <button className="hover:text-white">Changelog</button>
        </li>
      </ul>

      {/* Button */}
      <button className="text-sm px-4 py-2 rounded-full bg-purple-600 text-white hover:bg-purple-700 focus:ring focus:ring-purple-500">
        Join waitlist
      </button>
    </nav>
  );
};

export default Navbar;
