const element1 = document.querySelector(".p1");
const element2 = document.querySelector(".p2");
const element3 = document.querySelector(".card-text");
const element4 = document.querySelector(".btn");
const element5 = document.querySelector(".p3");
const element6 = document.querySelector(".p4");
const element7 = document.querySelector(".p5");
const element8 = document.querySelector(".card-title");

const card = document.querySelector(".card");
card.addEventListener("mouseover", (event) => {
  //element.style.setProperty('left', '0px');
  element1.classList.add("animate__animated", "animate__bounceInLeft");
  element1.style.setProperty("--animate-duration", "0.9s");
  element2.classList.add("animate__animated", "animate__bounceInLeft");
  element2.style.setProperty("--animate-duration", "1.4s");
  element3.classList.add("animate__animated", "animate__slideInUp");
  element3.style.setProperty("--animate-duration", "0.9s");
  element4.classList.add("animate__animated", "animate__slideInUp");
  element4.style.setProperty("--animate-duration", "1.4s");
  element5.classList.add("animate__animated", "animate__bounceInLeft");
  element5.style.setProperty("--animate-duration", "1.8s");
  element6.classList.add("animate__animated", "animate__bounceInLeft");
  element6.style.setProperty("--animate-duration", "2.4s");
  element7.classList.add("animate__animated", "animate__bounceInLeft");
  element7.style.setProperty("--animate-duration", "3s");
  element8.classList.add("animate__animated", "animate__slideInUp");
  element8.style.setProperty("--animate-duration", "0.6s");
});

card.addEventListener("mouseout", (event) => {
  element1.classList.remove("animate__animated", "animate__bounceInLeft");
  element2.classList.remove("animate__animated", "animate__bounceInLeft");
  element3.classList.remove("animate__animated", "animate__slideInUp");
  element4.classList.remove("animate__animated", "animate__slideInUp");
  element5.classList.remove("animate__animated", "animate__bounceInLeft");
  element6.classList.remove("animate__animated", "animate__bounceInLeft");
  element7.classList.remove("animate__animated", "animate__bounceInLeft");
  element8.classList.remove("animate__animated", "animate__slideInUp");
  // element.style.setProperty('left', '-99px');
});