const AboutPage = () => {
    return (
      <div className="min-h-screen w-screen bg-gray-900 p-12 flex flex-col items-center overflow-auto">
        <div className="w-full max-w-screen-xl bg-gray-800 shadow-2xl rounded-3xl p-12 flex flex-col">
          {/* Header */}
          <h1 className="text-5xl font-extrabold text-center text-white mb-8 tracking-tight">
            <span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
              About
            </span>
          </h1>
          <p className="text-lg text-gray-300 text-center mb-12 max-w-3xl mx-auto">
            Exploring ancient connections between Chinese and Sumerian through computational anthropology.
          </p>
  
          {/* Content Sections */}
          <div className="flex flex-col gap-8">
            {/* Background */}
            <div className="text-center">
              <h2 className="text-2xl font-semibold text-white mb-4">Background</h2>
              <p className="text-gray-300 max-w-2xl mx-auto">
                Inspired by <span className="font-semibold italic">Chinese and Sumerian</span> (1913) and claims of Western influence on Chinese civilization, this project investigates linguistic and visual links between Sumerian and Chinese using data science and computer vision.
              </p>
            </div>
  
            {/* Aims & Scope */}
            <div className="text-center">
              <h2 className="text-2xl font-semibold text-white mb-4">Aims & Scope</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="p-4 bg-gray-700 rounded-lg shadow-lg">
                  <p className="text-gray-300 text-sm">Compare Sumerian cuneiforms and Chinese Oracle Bone Characters with CV</p>
                </div>
                <div className="p-4 bg-gray-700 rounded-lg shadow-lg">
                  <p className="text-gray-300 text-sm">Text mining from Quora/YouTube</p>
                </div>
              </div>
            </div>
  
            {/* Deliverables */}
            <div className="text-center">
              <h2 className="text-2xl font-semibold text-white mb-4">Deliverables</h2>
              <ul className="text-gray-300 text-sm list-disc list-inside max-w-2xl mx-auto">
                <li>Public perceptions of Sumerian-Chinese links</li>
                <li>Similarity in writing systems (~2000 B.C.)</li>
              </ul>
            </div>
  
            {/* Abstract */}
            <div className="text-center">
              <h2 className="text-2xl font-semibold text-white mb-4">Abstract</h2>
              <p className="text-gray-300 max-w-2xl mx-auto">
                Using data science and computer vision, this project uncovers correlations between ancient China and Sumer via text mining (Quora/YouTube) and image alignment (*Chinese and Sumerian*), enhancing historical understanding.
              </p>
            </div>
          </div>
  
          <div className="mt-12 text-center">
            <a
              href="/methodology"
              className="bg-indigo-600 text-white px-8 py-3 text-lg rounded-lg shadow-lg transform transition hover:scale-105 hover:bg-indigo-700 mr-4"
            >
              Methodology
            </a>
          </div>
        </div>
      </div>
    );
  };
  
  export default AboutPage;