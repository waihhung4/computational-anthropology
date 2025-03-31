  const WordCloudPage = () => {
      const wordClouds = [
        { src: "/images/wordcloud/all_wordcloud.png", alt: "All Text Word Cloud" },
        { src: "/images/wordcloud/chinese_wordcloud.png", alt: "Chinese-related Text Word Cloud" },
        { src: "/images/wordcloud/sumerian_wordcloud.png", alt: "Sumerian-related Text Word Cloud" },
        { src: "/images/wordcloud/combined_wordcloud.png", alt: "Combination of Chinese and Sumerian Text Word Cloud" },
      ];
    
      return (
        <div className="min-h-screen w-screen bg-gray-900 p-12 flex flex-col items-center overflow-auto">
          <div className="w-full max-w-screen-xl bg-gray-800 shadow-2xl rounded-3xl p-12 flex flex-col">
            {/* Header */}
            <h1 className="text-5xl font-extrabold text-center text-white mb-8 tracking-tight">
              <span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
                Word Clouds
              </span>
            </h1>
            <p className="text-lg text-gray-300 text-center mb-12 max-w-3xl mx-auto">
              Visualizing key themes from 11,000+ texts using Gensim LDA.
            </p>
    
            {/* Word Clouds */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {wordClouds.map((cloud, index) => (
                <div key={index} className="flex flex-col items-center">
                  <img
                    src={cloud.src}
                    alt={cloud.alt}
                    className="w-full max-w-md h-auto rounded-lg shadow-lg"
                  />
                  <p className="text-gray-300 text-sm mt-2">{cloud.alt}</p>
                </div>
              ))}
            </div>
    
            {/* Call-to-Action */}
            <div className="mt-12 text-center">
              <a
                href="/results"
                className="bg-indigo-600 text-white px-8 py-3 text-lg rounded-lg shadow-lg transform transition hover:scale-105 hover:bg-indigo-700 mr-4"
              >
                Results
              </a>
              <a
                href="/methodology"
                className="bg-indigo-600 text-white px-8 py-3 text-lg rounded-lg shadow-lg transform transition hover:scale-105 hover:bg-indigo-700"
              >
                Methodology
              </a>
            </div>
          </div>
        </div>
      );
    };
    
    export default WordCloudPage;