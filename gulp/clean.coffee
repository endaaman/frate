del = require 'del'


g.task 'clean', (cb)->
    if conf.watching
        return cb()

    del [
        "#{conf.dest}/**/*"
        "!#{conf.bowerDir}"
        "!#{conf.bowerDir}/**/*"
    ], cb



g.task 'clean:cache', ['css:build', 'js:build', 'html:build'], (cb)->
    if not conf.prod
        return cb()

    del [
        "#{conf.dest}/.cache"
    ], cb
