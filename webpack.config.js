module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclued: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}