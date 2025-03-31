import React from "react";
import { Route, Routes } from 'react-router-dom';
import AboutPage from "./AboutPage.jsx";
import './App.css';
import ContentTableComponent from './ContentTableComponent.jsx';
import DataVisualizationPage from "./DataVisualizationPage.jsx";
import HomePage from './HomePage.jsx';
import ImageMappingTableComponent from './ImageMappingTableComponent.jsx';
import MethodologyPage from './MethodologyPage.jsx';
import Navbar from './Navbar.jsx';
import UrlTableComponent from './UrlTableComponent.jsx';
import WordCloudPage from "./WordCloudPage.jsx";


function App() {
  return (
    <div className="flex flex-col min-h-screen bg-gray-900 overflow-hidden items-center">
        <Navbar />
        <main className="flex-grow pt-20 px-12">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/methodology" element={<MethodologyPage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/results/content" element={<ContentTableComponent />} />
            <Route path="/results/url" element={<UrlTableComponent />} />
            <Route path="/results/imagemapping" element={<ImageMappingTableComponent />} />
            <Route path="/results/wordcloud" element={<WordCloudPage />} />
            <Route path="/visualization" element={<DataVisualizationPage />} />
            
          </Routes>
        </main>
      </div>
  );
}


const style = {
  container: {
    overflow: 'hidden',
    textAlign: 'center',
  },
};

export default App;