// Setup empty JS object to act as endpoint for all routes
projectData = {};
const serverPort = 8080;

// Require Express to run server and routes
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { response } = require('express');

// Start up an instance of app
const app = express();


/* Middleware*/
//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Cors for cross origin allowance
app.use(cors());

// Initialize the main project folder
app.use(express.static('website'));


// Setup Server
app.listen(serverPort, function () {
    console.log(`server is successfully running at localhost:${serverPort}`)
});

// get the projectData
app.get('/weatherGetter', (request, response) => {
    response.send(projectData);
});

app.post('/weatherPost', (request, response) => {
    projectData = {...request.body};
    response.end();
});