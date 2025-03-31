import { FaBrain, FaImage, FaPython } from "react-icons/fa"; // Optional: Remove if you want no graphics

const MethodologyPage = () => {
  return (
    <div className="min-h-screen w-screen bg-gray-900 p-12 flex flex-col items-center overflow-auto">
      <div className="w-full max-w-screen-xl bg-gray-800 shadow-2xl rounded-3xl p-12 flex flex-col">
        {/* Header */}
        <h1 className="text-5xl font-extrabold text-center text-white mb-8 tracking-tight">
          <span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
            Methodology
          </span>
        </h1>
        <p className="text-lg text-gray-300 text-center mb-12">
          Analyzing Chinese and Sumerian with computational tools.
        </p>

        {/* Methodology Sections */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Data Collection */}
          <div className="p-6 bg-gray-700 rounded-lg shadow-lg text-center transform transition hover:scale-105">
            <FaPython className="text-indigo-400 text-4xl mx-auto mb-4" /> {/* Optional */}
            <h2 className="text-2xl font-semibold text-white mb-2">Data Collection</h2>
            <ul className="text-gray-300 text-sm list-disc list-inside">
              <li>11,000+ texts</li>
              <li>YouTube/Quora</li>
              <li>Python scrapers</li>
            </ul>
          </div>

          {/* Text Analysis */}
          <div className="p-6 bg-gray-700 rounded-lg shadow-lg text-center transform transition hover:scale-105">
            <FaBrain className="text-indigo-400 text-4xl mx-auto mb-4" /> {/* Optional */}
            <h2 className="text-2xl font-semibold text-white mb-2">Text Analysis</h2>
            <ul className="text-gray-300 text-sm list-disc list-inside">
              <li>Tokenize, clean</li>
              <li>SiEBERT sentiment</li>
              <li>Gensim LDA topics</li>
            </ul>
          </div>

          {/* Image Analysis */}
          <div className="p-6 bg-gray-700 rounded-lg shadow-lg text-center transform transition hover:scale-105">
            <FaImage className="text-indigo-400 text-4xl mx-auto mb-4" /> {/* Optional */}
            <h2 className="text-2xl font-semibold text-white mb-2">Image Analysis</h2>
            <ul className="text-gray-300 text-sm list-disc list-inside">
              <li>Extract + refine</li>
              <li>ResNet/DinoV2</li>
              <li>Cosine similarity</li>
            </ul>
          </div>
        </div>

        {/* Technical Approach */}
        <div className="mt-12">
          <h2 className="text-3xl font-semibold text-white text-center mb-6">Technical Approach</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Scraping */}
            <div className="flex flex-col items-center">
              <h3 className="text-xl font-semibold text-white mb-2">Scraping</h3>
              <ul className="text-gray-300 text-sm list-none text-center">
                <li>Python</li>
                <li>11,000+ texts</li>
                <li>Linguistics data</li>
              </ul>
            </div>

            {/* Text Processing */}
            <div className="flex flex-col items-center">
              <h3 className="text-xl font-semibold text-white mb-2">Text Processing</h3>
              <ul className="text-gray-300 text-sm list-none text-center">
                <li>Tokenize, lemmatize, stop-word removal</li>
                <li>SiEBERT</li>
                <li>LDA</li>
              </ul>
            </div>

            {/* Image Processing */}
            <div className="flex flex-col items-center">
              <h3 className="text-xl font-semibold text-white mb-2">Image Processing</h3>
              <ul className="text-gray-300 text-sm list-none text-center">
                <li>Script + human</li>
                <li>ResNet/DinoV2</li>
                <li>Similarity</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MethodologyPage;