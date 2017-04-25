angular.module('opal.controllers').controller(
    'AsbestosExposureHistoryCtrl',
    function($http, scope, step, episode){
        "use strict";

        _.each(scope.editing.asbestos_exposure_history, function(aeh){
          var oh = _.findWhere(scope.editing.occupational_history, {
            id: aeh.related_occupation_id
          });
          if(oh){
            aeh.related_occupation_id = oh._client.id;
          }
        });

        scope.get_occupation_history = function(){
          if(!scope.editing.occupational_history || !scope.editing.occupational_history.length){
            return {};
          }
          else{
            var result = {};

            _.each(scope.editing.occupational_history, function(oh){
              var resultKey = oh.company_name;
              if(oh.start_year && oh.end_year){
                resultKey = resultKey + " " + oh.start_year + "-" + oh.end_year;
              }
              else if(oh.start_year || oh.end_year){
                resultKey = resultKey + " " + (oh.start_year || oh.end_year);
              }
              result[resultKey] = oh._client.id;
            });

            return result;
          }
        };
    });
