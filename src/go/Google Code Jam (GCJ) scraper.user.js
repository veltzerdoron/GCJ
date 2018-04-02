// ==UserScript==
// @name         Google Code Jam (GCJ) scraper
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Quickly scrape inputs and outputs from the Google Code Jam Website
// @author       Veltzer Doron
// @match        https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo/related?hl=en
// @grant        none
// @require    http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js
// @require    http://cdnjs.cloudflare.com/ajax/libs/sugar/1.3/sugar.min.js
// @include    https://code.google.com/codejam/contest/*
// ==/UserScript==

alert('Hello, GCJ scraping installed');


$(document).ready(function() {
  console.debug('Google code jam problem scraper setup');
  var $input = $('<input type="button" id="scraper" value="scrape" />');
  $input.click(function() {
    console.debug('Google code jam problem scraper running');
    // download inputs and outputs as in and example files
    console.debug('downloading inputs and outputs as in and example files');
    var i = 0;
    $('.problem-io-wrapper').each(function() {
      var letter = String.fromCharCode('A'.charCodeAt(0) + i);
      console.debug("Google code jam problem " + letter + " \'s input and output");
      var j = 0;
      $(this).find('code, pre.io-content').each(function() {
        var in_example = (j==0 ? "in" : "example");
        console.debug( in_example + ":");
        var content = encodeURIComponent(this.innerText.replace(/^[\s\n]/g, '').replace(/\n[\s\n]*\n/g, '\n'));  //remove multiple newlines and newlines from string start
        console.debug(content);
        var a = document.createElement("a");
        a.href = "data:text/plain;charset=utf-8," + content ;  //content
        a.download = letter + "-definition-0." + in_example;  //file name
        a.click();
        j++;
      });
      i++;
    });
    // download legend for problem names
    console.debug('downloading legend for problem names');
    var legend='';
    $('#dsb-problem-selection-list').find('[id^=dsb-problem-title]').each(function() {
        legend += this.innerText + '\n';  // add problem title to the legend content
    });
    console.debug(legend);
    var a = document.createElement("a");
    a.href = "data:text/plain;charset=utf-8," + legend;  //content
    a.download = "legend.txt";  //file name
    a.click();
  });
  $input.appendTo($('#logo-div'));
});