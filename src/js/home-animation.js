let opacity = 0;
const intervalID = 0;

const show = () => {
  const body = document.getElementById('body');
  const btn = document.querySelector('.button');
  if (body) {
    opacity = Number(window.getComputedStyle(body).getPropertyValue('opacity'));
    if (opacity < 1) {
      opacity = opacity + 0.1;
      setTimeout(() => {
        body.style.opacity = opacity;
      }, 200);
      setTimeout(() => {
        btn.style.opacity = opacity;
        btn.classList.add('bounce');
      }, 1200);
    } else {
      clearInterval(intervalID);
    }
  }
};

const fadeIn = () => {
  setInterval(show, 200);
};

window.onload = fadeIn;
