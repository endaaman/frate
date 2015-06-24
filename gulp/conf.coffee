fs = require 'fs'
argv = require('yargs').argv
dateFormat = require 'dateformat'


class Conf
    constructor: ->
        @hash = dateFormat (new Date()), 'yyyymmddhhMMss'
        @src = 'client'
        @static = 'assets'
        @bowerDir = (try
            JSON.parse(fs.readFileSync '.bowerrc', 'utf8').directory ? throw 'e'
        catch error
            'bower_components'
        )
        @ngAppName = 'endaApp'

        @prod = !!argv.prod
        @dest = if @prod then 'dist' else 'public'
        @minify = !argv.skipmin
        @seeding = !!argv.seed

        @watching = false

module.exports = new Conf()
