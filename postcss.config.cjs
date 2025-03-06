//const autoprefixer = require('autoprefixer');
const preset = require('postcss-preset-env');

const mode = process.env.NODE_ENV;
const dev = mode === "development";

const config = {
	plugins: [
    //autoprefixer,
    preset({stage: 1})
  ]
};

module.exports = config;


