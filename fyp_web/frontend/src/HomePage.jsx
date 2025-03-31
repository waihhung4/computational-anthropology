import { NavLink } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="min-h-screen h-screen w-screen bg-gray-900 p-12 flex flex-col items-center overflow-auto">
      <div className="w-full h-full bg-white shadow-2xl rounded-3xl p-12 flex flex-col">
        <h1 className="text-5xl font-extrabold text-center text-gray-800 mb-8">
          Computational Anthropology Between Chinese and Sumerian
        </h1>
        <p className="text-lg text-gray-600 text-center mb-6">
          Inspired by the book <span className="font-semibold">Chinese and Sumerian</span>, this project explores linguistic properties between the two languages using computational methods.
        </p>
        
        <div className="relative w-full h-64 bg-cover bg-center rounded-xl shadow-lg mb-8 flex-shrink-0" 
             style={{ backgroundImage: "url('/images/abstract-linguistics.jpg')" }}>
          <div className="w-full h-full flex items-center justify-center bg-black bg-opacity-50 rounded-xl">
            <h2 className="text-4xl text-white font-bold">Unveiling Ancient Connections</h2>
          </div>
        </div>
        
        <div className="mt-8 flex-grow">
          <h2 className="text-3xl font-semibold text-gray-700 mb-6">Overview</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 bg-gray-50 rounded-lg shadow-lg text-center">
              <h3 className="text-xl font-semibold text-gray-800 mb-2">Data Collection</h3>
              <p className="text-gray-600">Over 11,000 texts scraped from YouTube and Quora using Python-based scrapers.</p>
            </div>
            
            <div className="p-6 bg-gray-50 rounded-lg shadow-lg text-center">
              <h3 className="text-xl font-semibold text-gray-800 mb-2">Text Analysis</h3>
              <p className="text-gray-600">Preprocessed and analyzed using Sentiment Analysis, Topic Modeling, and Word Clouds.</p>
            </div>

            <div className="p-6 bg-gray-50 rounded-lg shadow-lg text-center">
              <h3 className="text-xl font-semibold text-gray-800 mb-2">Character Image Analysis</h3>
              <p className="text-gray-600">Extracting character images from the book to perform AI-driven image similarity analysis using cosine similarity.</p>
            </div>
          </div>
        </div>
        
        <div className="mt-8 text-center flex-shrink-0">
          <NavLink to="/about">
            <button className="bg-blue-600 text-white px-8 py-3 text-lg rounded-lg shadow-lg transform transition hover:scale-105 hover:bg-blue-700">
              Explore More
            </button>
          </NavLink>
          
        </div>
      </div>
    </div>
  );
}


export default HomePage;