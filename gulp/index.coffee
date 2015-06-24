global.g = require 'gulp'
global.$ = do require 'gulp-load-plugins'
global.conf = require './conf'

require './clean'
require './copy'
require './build-css'
require './build-html'
require './build-js'
require './build'
require './serve'
require './watch'

g.task 'default', ['watch']
