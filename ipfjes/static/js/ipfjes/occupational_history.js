angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function($http, scope, step, episode){
        "use strict"
        scope.get_soc_details = function(editing){
            return '/soc/details/?title=' + editing.soc_job
        };

        scope.$watch(scope.editing, "occupational_history", function(){
          _.each(scope.editing.occupational_history, function(oh){
            if(!oh._client){
              oh._client = {};
            }

            if(!oh._client.id){
              oh._client.id = _.uniqueId("occupational_history");
            }
          });
        });

        scope.preSave = function(editing){
          _.each(editing.occupational_history, function(oh){
            oh.occupational_history_client_id = oh._client.id;
          });
        };
    });
