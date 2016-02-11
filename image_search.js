// This requires Node.js
// Dependency of AAR Project 2015-2016
// Written by Gautam Mittal

var Bing = require('node-bing-api')({ accKey: process.argv[2] });

Bing.images(process.argv[3], {
  imageFilters: {
    size: 'medium',
    style: 'graphics'
  }
}, function(error, res, body){
console.log(JSON.stringify(body));
});
