import React, { useState } from 'react';
import { VideoUploader } from './components/VideoUploader';
import { NumberInput } from './components/NumberInput';
import { uploadVideo } from './api/uploadService';
import { UploadStatus } from './types';

function App() {
  const [numVideos, setNumVideos] = useState<number>(0);
  const [showUpload, setShowUpload] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState<string[]>([]);
  const [uploadStatus, setUploadStatus] = useState<UploadStatus>({ uploading: false });

  const handleNumVideosSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setShowUpload(true);
  };

  const handleFileUpload = async (index: number, file: File) => {
    try {
      setUploadStatus({ uploading: true });
      const filename = await uploadVideo(file);
      setUploadedFiles(prev => {
        const newFiles = [...prev];
        newFiles[index] = filename;
        return newFiles;
      });
    } catch (error) {
      setUploadStatus({ 
        uploading: false, 
        error: error instanceof Error ? error.message : 'Upload failed'
      });
    } finally {
      setUploadStatus(prev => ({ ...prev, uploading: false }));
    }
  };

  const handleReset = () => {
    setShowUpload(false);
    setUploadedFiles([]);
    setNumVideos(0);
    setUploadStatus({ uploading: false });
  };

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center mb-6">Video Upload</h1>
        
        {!showUpload ? (
          <NumberInput 
            value={numVideos}
            onChange={setNumVideos}
            onSubmit={handleNumVideosSubmit}
          />
        ) : (
          <div className="space-y-4">
            {Array.from({ length: numVideos }).map((_, index) => (
              <VideoUploader
                key={index}
                index={index}
                onFileSelect={handleFileUpload}
                uploadedFile={uploadedFiles[index]}
                disabled={uploadStatus.uploading}
              />
            ))}
            <button
              onClick={handleReset}
              className="w-full bg-gray-500 text-white rounded-md py-2 hover:bg-gray-600 transition-colors disabled:bg-gray-300"
              disabled={uploadStatus.uploading}
            >
              Reset
            </button>
          </div>
        )}
        
        {uploadStatus.uploading && (
          <div className="mt-4 text-center text-sm text-gray-600">
            Uploading video...
          </div>
        )}
        
        {uploadStatus.error && (
          <div className="mt-4 text-center text-sm text-red-600">
            {uploadStatus.error}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;