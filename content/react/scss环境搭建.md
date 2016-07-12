Date: 7/12/2016 11:04:38 AM  
Title:SCSS的环境配置 
##SCSS的环境配置
#####外部依赖说明
1. node的版本：node-v0.12.8-x64
2. ruby的版本:rubyinstaller_V2.2.2.95_setup
#####node安装所需要的js文件
以下这些最好安装到项目的目录文件夹下

1. node install gulp -g
2. node install gulp-util
3. node install gulp-ruby-sass
4. node install gulp-autoprefixer
5. gem install sass 这是ruby的命令
#####本地的配置文件
与scss同级目录下，先建立一个gulpfile.js文件
     
     use strict;
     var gulp = require('gulp');
     var sass = require('gulp-ruby-sass');
     var autoprefixer = require('gulp-autoprefixer');

     gulp.task('default', function () {
       return sass('scss/*.scss', { style: 'compressed', noCache: true })
       .on('error', function (err) {
       console.error('Error!', err.message);
    })
       .pipe(autoprefixer())
       .pipe(gulp.dest('css/'));
    });

      gulp.task('watch', function () {
      gulp.watch('scss/*.scss', ['default']);
    });
   
然后命令行当前目录切换到存放gulp.js的目录下后，执行gulp。
