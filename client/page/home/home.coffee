'use strict'

angular.module modulePage
.config ($stateProvider) ->
    $stateProvider
    .state 'home',
        url: '/'
        templateUrl: '/page/home/home.html'
        controller: 'HomeCtrl'

.controller 'HomeCtrl',
    ($scope, $state) ->
        $scope.message = 'おちんこ漢字'
