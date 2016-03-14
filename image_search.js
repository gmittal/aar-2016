// This requires Node.js
/* Runs image search query through Bing API,
   grabs a list of 50 image URLs, and chooses a random one */
// Dependency of AAR Project 2015-2016
// Written by Gautam Mittal

var Bing = require('node-bing-api')({ accKey: process.argv[2] });
var topResults = 10;
Bing.images(process.argv[3] + "clip art png", {
  imageFilters: {
    // size: 'medium'

    // style: 'graphics'
  }
}, function(error, res, body){
  if (error) {
    console.log("ERR");
    process.exit();
  } else {
      var urls = [];
      for (var i = 0; i < body["d"]["results"].length; i++) {
        urls.push(body["d"]["results"][i].MediaUrl);
      }

      var randomIndex = Math.floor(Math.random() * topResults) + 0;
      console.log(urls[randomIndex]);
  }

});
