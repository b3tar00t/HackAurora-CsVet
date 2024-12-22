import React, { useState } from "react";

const Dashboard = () => {
  const [file, setFile] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  // Video upload handlers
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setResponseData(null);
    setProgress(0);
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setError(null);
    setProgress(30);

    try {
      const response = await fetch("http://localhost:8000/upload/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload file.");
      }

      setProgress(70);
      const data = await response.json();
      setResponseData(data);
      setProgress(100);
      setError(null);
    } catch (err) {
      console.error("Error uploading file:", err);
      setError("Error uploading file. Please try again.");
      setProgress(0);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-br from-black via-gray-900 to-purple-900 text-white">
      <div className="w-full max-w-lg p-8 bg-gray-800 bg-opacity-90 rounded-xl shadow-lg">
        <h1 className="text-4xl font-bold text-center text-purple-400 mb-6">
          Lets Create!
        </h1>

        <div>
          <h2 className="text-2xl font-semibold mb-4 text-gray-300">
            Upload Your Video
          </h2>
          <input
            type="file"
            accept=".mp4"
            onChange={handleFileChange}
            className="block w-full text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100"
          />
          <button
            onClick={handleUpload}
            className={`mt-4 w-full bg-purple-600 text-white font-bold py-2 px-4 rounded ${
              loading || !file ? "opacity-50 cursor-not-allowed" : ""
            }`}
            disabled={loading || !file}
          >
            {loading ? "Uploading..." : "Upload & Analyze"}
          </button>

          <div className="mt-4 bg-gray-700 rounded h-2 w-full">
            {progress > 0 && (
              <div
                className="h-2 bg-purple-500"
                style={{ width: `${progress}%` }}
              />
            )}
          </div>

          {error && <p className="text-red-500 mt-2">{error}</p>}
          {responseData && (
            <div className="mt-4 bg-gray-900 p-4 rounded">
              <h3 className="text-lg font-bold">Response:</h3>
              <p>{responseData.message}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
