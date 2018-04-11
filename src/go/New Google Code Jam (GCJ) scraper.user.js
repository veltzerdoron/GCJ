// ==UserScript==
// @name         New Google Code Jam (GCJ) scraper
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Quickly scrape inputs and outputs from the Google Code Jam Website
// @author       Veltzer Doron
// @match        https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo/related?hl=en
// @grant        none
// @require      http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js
// @require      http://cdnjs.cloudflare.com/ajax/libs/sugar/1.3/sugar.min.js
// @include      https://codejam.withgoogle.com/2018/*
// run-at        document-end
// ==/UserScript==

alert('Hello, GCJ scraping installed');


$(document).ready(function() {
  console.debug('Google code jam problem scraper setup');
  var $input = $('<input type="button" id="scraper" value="scrape" />');
  $input.click(function() {
    console.debug('Google code jam problem scraper running');

    // download legend for problem names and click the various problems to cause them to load
    var legend='';
    var i = 0;
    var j = 0;
    console.debug('downloading legend file for problem names');
    $('.task-list').find('a').each(function() {
      if ($(this).hasClass('active')) {
        var letter = String.fromCharCode('A'.charCodeAt(0) + i);
        console.debug("Google code jam problem " + letter + " \'s input and output");
        var j = 0;
        $('.problem-io-wrapper').find('pre.io-content').each(function() {
          // download inputs and outputs as input and def files
          var in_example = (j==0 ? "input" : "def");
          var content = encodeURIComponent(this.innerText.replace(/^[\s\n]/g, '').replace(/\n[\s\n]*\n/g, '\n'));  //remove multiple newlines and newlines from string start
          console.debug( in_example + ":" + content);
          var a = document.createElement("a");
          a.href = "data:text/plain;charset=utf-8," + content ;  //content
          a.download = letter + "-" + in_example + ".txt";  //file name
          a.click();
          j++;
        });
      }
      legend += String(i + 1) + '.' + this.innerText + '\n';  // add problem title to the legend content
      i++;
    });
    console.debug(legend);
    var a = document.createElement("a");
    a.href = "data:text/plain;charset=utf-8," + legend;  //content
    a.download = "legend.txt";  //file name
    a.click();
  });
  $input.appendTo($('.challenge__title'));
});