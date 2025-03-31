import { FaChartLine, FaObjectGroup } from "react-icons/fa";

const DataVisualizationPage = () => {
  return (
    <div className="min-h-screen w-screen bg-gray-900 p-12 flex flex-col items-center overflow-auto">
      <div className="w-full max-w-screen-xl bg-gray-800 shadow-2xl rounded-3xl p-12 flex flex-col">
        {/* Header */}
        <h1 className="text-5xl font-extrabold text-center text-white mb-8 tracking-tight">
          <span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
            Data Visualization
          </span>
        </h1>
        <p className="text-lg text-gray-300 text-center mb-12">
          Exploring word embeddings and topic clusters through advanced visualizations.
        </p>

        {/* Shepard Diagram Section */}
        <div className="mt-12">
          <div className="flex items-center justify-center mb-4">
            <FaChartLine className="text-indigo-400 text-3xl mr-2" />
            <h2 className="text-3xl font-semibold text-white">Shepard Diagram for Distance Preservation</h2>
          </div>
          <img
            src="/images/data_visualization/shepard_diagram.png"
            alt="Shepard Diagram comparing PCA and t-SNE for distance preservation"
            className="w-full h-auto rounded-lg shadow-md max-w-3xl mx-auto"
          />
          <p className="text-gray-300 text-center mt-4">
            Comparing distance preservation of PCA and t-SNE in reduced dimensions.
          </p>
        </div>

        {/* Selective Word Embedding Visualization Section */}
        <div className="mt-12">
          <div className="flex items-center justify-center mb-4">
            <FaChartLine className="text-indigo-400 text-3xl mr-2" />
            <h2 className="text-3xl font-semibold text-white">Selective Word Embedding Visualization (PCA+t-SNE)</h2>
          </div>
          <img
            src="/images/data_visualization/word_embedding.png"
            alt="Word Embedding Visualization with PCA and t-SNE"
            className="w-full h-auto rounded-lg shadow-md max-w-3xl mx-auto"
          />
          {/* Metrics Section */}
          <div className="mt-6 max-w-3xl mx-auto bg-gray-700 p-4 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold text-white text-center mb-2">Evaluation Metrics</h3>
            <div className="text-gray-300 text-sm grid grid-cols-1 md:grid-cols-3 gap-4">
              <p><strong>Final KL Divergence:</strong> 2.7796</p>
              <p><strong>Trustworthiness Score:</strong> 0.9813</p>
              <p><strong>Spearman Correlation:</strong> 0.6883</p>
            </div>
          </div>
          <p className="text-gray-300 text-center mt-4">
            Visualizing word embeddings reduced to 2D using PCA and t-SNE.
          </p>
        </div>

        {/* Topic Clustering Visualization Section */}
        <div className="mt-12">
          <div className="flex items-center justify-center mb-4">
            <FaObjectGroup className="text-indigo-400 text-3xl mr-2" />
            <h2 className="text-3xl font-semibold text-white">Topic Clustering Visualization</h2>
          </div>
          <img
            src="/images/data_visualization/clustering.png"
            alt="Topic Clustering using KMeans with 21 clusters"
            className="w-full h-auto rounded-lg shadow-md max-w-3xl mx-auto"
          />
          <p className="text-gray-300 text-center mt-4">
            Clustering of topics using KMeans with 14 clusters on vectorized data.
          </p>
        </div>
      </div>
    </div>
  );
};

export default DataVisualizationPage;