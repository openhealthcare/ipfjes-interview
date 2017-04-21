angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function(SocCodeService, scope, step, episode){
        "use strict"
        scope.get_soc_details = function(editing){
            return '/soc/details/?title=' + editing.soc_job
        };

        scope.socCodes = {};
        scope.aspestos_risk = {};

        SocCodeService.load().then(function(data){
          _.each(data, function(d){
            scope.socCodes[d.title] = d;
          });
        });

        scope.initialise = function(){
          // if we've got an asbestos_exposure_history for this
          // occupational history, put it on a var in _client
          // and remove it from the standard list
          _.each(scope.editing.occupational_history, function(oh){
            if(!oh._client){
              oh._client = {id: _.uniqueId("occupational_history")};
            }

            var nestedAeh = {};

            if(oh.id){
              var foundNestedAeh = _.findWhere(scope.editing.asbestos_exposure_history, {related_occupation_id: oh.id});
              scope.editing.asbestos_exposure_history = _.filter(scope.editing.asbestos_exposure_history, function(aeh){
                return aeh.related_occupation_id !== oh.id;
              });

              if(foundNestedAeh){
                nestedAeh = foundNestedAeh;
              }
            }
            nestedAeh.related_occupation_id = oh._client.id;

            oh._client.aeh = {
              asbestos_exposure_history: nestedAeh
            };
          });

          // load in the code service
          SocCodeService.load().then(function(data){
            _.each(data, function(d){
              scope.socCodes[d.title] = d;
            });
          });
        };

        scope.$watch(scope.editing, "occupational_history", function(){
          _.each(editing.occupational_history, function(oh){
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
            if(scope.socCodes[oh.soc_job]){
              editing.asbestos_exposure_history.push(oh._client.aeh.asbestos_exposure_history);
            }
          });
        };

        scope.initialise();
    });
