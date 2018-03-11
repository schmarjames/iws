var gulp          = require('gulp');
var notify        = require('gulp-notify');
var source        = require('vinyl-source-stream');
var browserify    = require('browserify');
var babelify      = require('babelify');
var browserSync   = require('browser-sync').create();
var rename        = require('gulp-rename');
var uglify        = require('gulp-uglify');
var merge         = require('merge-stream');
var sass          = require('gulp-sass');
var concat        = require('gulp-concat');

var jsFiles       = "app/**/*.js";
var sassFiles     = "app/**/*.scss";
var viewFiles     = "app/**/*.html";

var interceptErrors = function(error) {
  var args = Array.prototype.slice.call(arguments);

  // Send error to notification center with gulp-notify
  notify.onError({
    title: 'Compile Error',
    message: '<%= error.message %>'
  }).apply(this, args);

  // Keep gulp from hanging on this task
  this.emit('end');
};

gulp.task('browserify', function() {
  return browserify('./app/js/init.js')
      .transform(babelify, {presets: ["es2015"]})
      .bundle()
      .on('error', interceptErrors)
      //Pass desired output filename to vinyl-source-stream
      .pipe(source('main.js'))
      // Start piping stream to tasks!
      .pipe(gulp.dest('./build/'));
});

gulp.task('html', function() {
  return gulp.src("index.html")
      .on('error', interceptErrors)
      .pipe(gulp.dest('./build/'));
});

gulp.task('sass', function() {
  return gulp.src(sassFiles)
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(concat('main.css'))
    .pipe(gulp.dest('./build'));
});

// This task is used for building production ready
// minified JS/CSS files into the dist/ folder
gulp.task('build', ['html', 'browserify'], function() {
  var html = gulp.src("build/index.html")
                 .pipe(gulp.dest('./dist/'));

  var css = gulp.src("build/main.css")
                .pipe(gulp.dest('./dist/'));

  var js = gulp.src("build/main.js")
               .pipe(gulp.dest('./dist/'));

  var pjson = gulp.src("package.json")
                  .pipe(gulp.dest('./dist/'));

  var nodeServer = gulp.src("index.js")
                       .pipe(gulp.dest('./dist/'));

  return merge(html, css, js, pjson, nodeServer);
});

gulp.task('default', ['html', 'browserify', 'sass'], function() {

  browserSync.init(['./build/**/**.**'], {
    server: "./build",
    port: 4000,
    notify: false,
    ui: {
      port: 4001
    }
  });

  gulp.watch("index.html", ['html']);
  gulp.watch(jsFiles, ['browserify']);
  gulp.watch(sassFiles, ['sass']);
});
