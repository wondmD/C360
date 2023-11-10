// loader.js
document.addEventListener("DOMContentLoaded", function () {
    var loader = document.getElementById("loader");
    var content = document.getElementById("content");
    loader.style.display = "block";
    content.style.display = "none";
  });
  
  window.addEventListener("load", function () {
    var loader = document.getElementById("loader");
    var content = document.getElementById("content");
  
    setTimeout(function () {
      // Hide the loader after a slight delay
      loader.style.display = "none";
      content.style.display = "block";
    }, 2000); // Adjust the delay time (in milliseconds) as needed
  });
  