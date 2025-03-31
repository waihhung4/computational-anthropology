const path = require('path');

module.exports = {
  webpack: {
    configure: (webpackConfig) => {
      webpackConfig.resolve.alias['@'] = path.resolve(__dirname, 'src/');
      return webpackConfig;
    },
  },
};