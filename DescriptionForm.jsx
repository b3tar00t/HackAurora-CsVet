import React from "react";

const DescriptionForm = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic for handling descriptions
    alert("Description submitted!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2 className="text-xl mb-4">Describe your video requirements</h2>
      <textarea
        className="w-full p-2 border rounded mb-4"
        placeholder="Describe how you want the videos..."
        rows="6"
      ></textarea>
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Submit
      </button>
    </form>
  );
};

export default DescriptionForm;
