const express = require('express');
const app = express();

app.use(express.static(__dirname + '/public'));

const port = 3000; // Change to your desired port number

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
