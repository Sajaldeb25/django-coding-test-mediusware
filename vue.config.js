const path = require('path');

module.exports = {
    publicPath: './src/static/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, './src/static/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
        writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    },
    pluginOptions: {
        sourceDir: './src/templates/assets/js', // Required for plugin. Does nothing if not entered
        entryFile: "main.js" // Defaults to "main.js" if not specified
    },
    css : {
        extract : true
    }


}