'use strict'

window.moduleConfig = 'endaConfig'

angular.module moduleConfig, [
    moduleCore
    modulePage
    'angular-google-analytics'
]

.config ($locationProvider)->
    $locationProvider
    .html5Mode true
    .hashPrefix '!'

.config ($urlRouterProvider, $urlMatcherFactoryProvider)->
    $urlRouterProvider.rule ($injector, $location)->
        path = $location.url()
        replaced = false

        if path isnt '/'
            if path.indexOf('/?') > 0
                replaced = true
                path = path.replace '/?', '?'

            if path[path.length - 1] is '/'
                replaced = true
                path = path.replace /\/$/, ''

        if replaced
            return path
        else
            return false

    # $urlRouterProvider.otherwise ($injector)->
    #     $injector.get('NotFound')()
