angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function(scope, step, episode, SocCodeService){
        "use strict";

        var getClient = function(oh){
          if(!oh){
            oh = {};
          }
          var clientDefaults = {
            // the id used in the name
            id: _.uniqueId("occupational_history"),
            aeh: {},
            // the job matches for the lookup
            matches: [],

            // the job that has been selected but not confirmed
            job: null
          };

          // whether we're in the edit mode for the job

          clientDefaults.editJob = !oh.soc_job;

          var existingClient = oh._client || {};

          return _.extend(clientDefaults, existingClient);
        };

        scope.select = function(job, client){
          client.job = job;
        };

        scope.filterChanged = function(client){
          if(client.soc_job_filter && client.soc_job_filter.length > 2){
            client.matches = _.filter(scope.socjob_list, function(j){
              return j.toLowerCase().indexOf(client.soc_job_filter.toLowerCase()) != -1;
            });
          }
        };

        scope.confirm = function(oh){
          oh.soc_job = oh._client.job || oh._client.soc_job_filter;
          oh._client.soc_job_filter = null;
          oh._client.editJob = false;
        };

        scope.get_soc_details = function(client){
          if(client.job){
            return '/soc/details/?title=' + client.job;
          }
        };

        scope.switchToEditJob = function(client){
          client.editJob = true;
        };

        // this function overrides the pathway directive's add another
        scope.addAnother = function(){
            var c = getClient();
            c.completed = false;
            scope.editing.occupational_history.push({_client: c});
        };

        scope.socCodes = {};
        scope.aspestos_risk = {};

        SocCodeService.load().then(function(data){
          _.each(data, function(d){
            scope.socCodes[d.title] = d;
          });
        });

        scope.initialise = function(){
          if(!scope.editing.occupational_history.length){
            var oh = {_client: getClient()};
            oh._client.completed = false;
            scope.editing.occupational_history.push(oh);
          }
          else{
            // if we've got an asbestos_exposure_history for this
            // occupational history, put it on a var in _client
            // and remove it from the standard list
            _.each(scope.editing.occupational_history, function(oh){
              oh._client = getClient(oh);

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
          }
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

            oh._client = getClient(oh);
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
