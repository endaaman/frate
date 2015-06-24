url = require 'url'
proxy = require 'proxy-middleware'
modRewrite  = require 'connect-modrewrite'
browserSync = require 'browser-sync'

require './serve'


g.task 'serve', ['build'], ->
    makeProxy = (path)->
        proxyOptions = url.parse "http://localhost:8000#{path}"
        proxyOptions.route = path
        proxy proxyOptions

    baseDir = if conf.prod then "#{conf.dest}/" else ["#{conf.dest}/", "#{conf.static}/"]

    browserSync
        port: 9000
        notify: false
        open: false
        server:
            baseDir: baseDir
            middleware: [
                makeProxy '/api/'
            ,
                makeProxy '/admin/'
            ,
                makeProxy '/media/'
            ,
                makeProxy '/static/'
            ,
                modRewrite [
                    '(.+)/$ $1 [R]'
                    '^(.+)/\\?(.+)$ $1?$2 [R]'
                    '!\\.\\w+$ /index.html [L]'
                ]
            ]
