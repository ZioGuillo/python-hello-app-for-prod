document.addEventListener("DOMContentLoaded", function() {
  var sectionElements = document.querySelectorAll('.section');

  sectionElements.forEach(function(sectionElement) {
    var boxElements = sectionElement.querySelectorAll('.box');
    if (boxElements.length > 5) {
      sectionElement.classList.add('disabled-justify');
    } else {
      sectionElement.classList.remove('disabled-justify');
    }
  });
});