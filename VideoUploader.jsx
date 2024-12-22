import React, { useState } from "react";

const VideoUploader = ({ numVideos, onComplete }) => {
  const [uploadedVideos, setUploadedVideos] = useState(0);

  const handleUpload = () => {
    setUploadedVideos((prev) => prev + 1);
  };

  return (
    <div>
      <h2 className="text-xl mb-4">Upload {numVideos} videos</h2>
      {Array.from({ length: numVideos }, (_, i) => (
        <div key={i} className="mb-4">
          <input
            type="file"
            accept="video/*"
            className="w-full p-2 border rounded"
            onChange={handleUpload}
          />
        </div>
      ))}
      {uploadedVideos >= numVideos && (
        <button
          className="bg-purple-500 text-white px-4 py-2 rounded"
          onClick={onComplete}
        >
          Proceed to Description
        </button>
      )}
    </div>
  );
};

export default VideoUploader;
