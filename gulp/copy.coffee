

g.task 'copy:static', (cb)->
    if not conf.prod
        return cb()
    g.src ["#{conf.static}/**/*"]
    .pipe g.dest "#{conf.dest}/"

g.task 'copy', ['copy:static']
