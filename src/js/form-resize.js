var windowSize = window.matchMedia('(max-width: 860px)');

let formBorder = document.querySelector('.form-container');
let rightForm = document.querySelector('.form-right');
let formWrapper = document.querySelector('.form__wrapper');

windowSize.onchange = (e) => {
  if (e.matches && rightForm) {
    formBorder.style.borderRadius = '5px 0 0 5px';
  } else if (e.matches && !rightForm) {
    formBorder.style.borderRadius = '5px';
  }
};
