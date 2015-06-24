browserSync = require 'browser-sync'


g.task 'watch:css:vendor', ['css:vendor'], ->
    browserSync.reload()
g.task 'watch:css:common', ['css:common'], ->
    browserSync.reload()
g.task 'watch:css:app', ['css:app'], ->
    browserSync.reload()
g.task 'watch:js', ['js'], ->
    browserSync.reload()
g.task 'watch:html', ['html'], ->
    browserSync.reload()
g.task 'watch:index', ['index'], ->
    browserSync.reload()


g.task 'watch', ['build', 'serve'], (cb)->
    if conf.prod
        return cb()
    conf.watching = true
    g.watch "#{conf.src}/vendor/**/*.{sass,scss}", ['watch:css:vendor']
    g.watch "#{conf.src}/style/**/*.{sass,scss}", ['watch:css:common']
    g.watch "#{conf.src}/{page,component}/**/*.{sass,scss}", ['watch:css:app']
    g.watch "#{conf.src}/**/*.coffee", ['watch:js']
    g.watch "#{conf.src}/{page,core,component}/**/*.jade", ['watch:html']
    g.watch "#{conf.src}/index.jade", ['watch:index']
