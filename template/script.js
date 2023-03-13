let currentSlide = 1;

function showSlide(n) {
  let slides = document.getElementsByClassName("slide");
  if (n > slides.length) {
    currentSlide = slides.length - 1;
  }
  if (n < 1) {
    currentSlide = 1;
  }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[currentSlide - 1].style.display = "flex";
}

function nextSlide() {
  showSlide(currentSlide++);
}

function prevSlide() {
  showSlide(currentSlide--);
}

// Add keyboard event listeners
document.addEventListener("keydown", function(event) {
  if (event.keyCode === 37) {  // Left arrow
    prevSlide();
  }
  else if (event.keyCode === 39) {  // Right arrow
    nextSlide();
  }
});


document.addEventListener("DOMContentLoaded", function() {
  showSlide(currentSlide);
});
