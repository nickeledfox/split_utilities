const { src, dest, watch, parallel } = require('gulp');
const uglify = require('gulp-uglify-es').default;
const concatCss = require('gulp-concat-css');
const cssMinify = require('gulp-css-minify');
const concat = require('gulp-concat');
const del = require('del');

function scripts() {
  return src('src/js/**/*.js')
    .pipe(concat('main.min.js'))
    .pipe(uglify())
    .pipe(dest('static/js'));
}

function styles() {
  return src('src/**/*.css')
    .pipe(concatCss('bundle.css'))
    .pipe(cssMinify())
    .pipe(dest('static/css'));
}

function clean() {
  return del(['static/css', 'static/js']);
}

function watching() {
  watch(['src/css/**/*.css'], styles);
  watch(['src/js/**/*.js'], scripts);
}

exports.scripts = scripts;
exports.styles = styles;
exports.watching = watching;
exports.clean = clean;

exports.default = parallel(clean, styles, scripts, watching);
