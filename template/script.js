let currentSlide = 0;

function showSlide(n) {
  let slides = document.getElementsByClassName("slide");
  currentSlide = Math.min(currentSlide, slides.length - 1);
  currentSlide = Math.max(currentSlide, 0);

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[currentSlide].style.display = "flex";
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
