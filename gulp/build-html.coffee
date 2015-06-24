lazypipe = require 'lazypipe'
bowerFiles = require 'main-bower-files'


g.task 'html', ->
    dest = if conf.prod then "#{conf.dest}/.cache/" else "#{conf.dest}/"

    target = [
        "#{conf.src}/**/*.jade"
        "!#{conf.src}/index.jade"
    ]

    minifyAndTemplate = lazypipe()
    .pipe $.minifyHtml,
        spare: true
        empty: true
        conditionals: true
        quotes: true
    .pipe $.angularTemplatecache, 'templates.js',
        module: conf.ngAppName
        root: '/'

    g.src target
    .pipe $.jade pretty: not conf.prod
    .pipe $.if conf.prod, minifyAndTemplate()
    .pipe g.dest dest


g.task 'html:build', ['html'], (cb)->
    cb()


g.task 'index', ['js:build', 'css:build', 'html:build', 'clean:cache'], ->
    ignorePath = ["#{conf.dest}/"]
    target = ''
    if conf.prod
        target = [
            "#{conf.dest}/*.js"
            "#{conf.dest}/*.css"
        ]
    else
        target = [
            "#{conf.dest}/vendor/**/*.css"
            "#{conf.dest}/style/**/*.css"
            "#{conf.dest}/app.css"

            "#{conf.dest}/core/*.js"
            "#{conf.dest}/core/**/*.js"
            "#{conf.dest}/component/*.js"
            "#{conf.dest}/component/**/*.js"
            "#{conf.dest}/page/*.js"
            "#{conf.dest}/page/**/*.js"
            "#{conf.dest}/config/*.js"
            "#{conf.dest}/config/**/*.js"
            "#{conf.dest}/app.js"
        ]

    g.src "#{conf.src}/index.jade"
    .pipe $.jade pretty: not conf.prod
    .pipe $.inject g.src(target), ignorePath: ignorePath
    .pipe($.if(conf.prod,
        $.if(conf.minify,
            $.minifyHtml
                spare: true
                empty: true
                conditionals: true
                quotes: true
                comments: true
        ),
        $.inject(g.src(bowerFiles(), base: conf.bowerDir, read: false ),{
            ignorePath: ignorePath
            name: 'bower'
        })))

    .pipe g.dest "#{conf.dest}/"
