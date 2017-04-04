angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function($http, scope, step, episode){
        "use strict"
        scope.hello_world = 'HELLO BEAUTIFUL WORLDS';
        scope.get_soc_details = function(editing){
            return '/soc/details/?title=' + editing.soc_job
        }
    });
