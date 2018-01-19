angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function(scope, step, episode, SocCodeService){
        "use strict";

        var getClient = function(oh){
            if(!oh){
                oh = {};
            }
            var client_id = _.uniqueId("occupational_history");
            var clientDefaults = {
                // the id used in the name
                id: client_id,
                // the list of asbestos exposure histories
                aeh: [],
                // the asbestos screening, only used if they have asbestos exposure history
                aes: {
                  asbestos_exposure_screening: {
                    _client: {
                      id: _.uniqueId("asbestos_screening"),
                    }
                  }
                },
                // the job matches for the s
                matches: [],
                // the job that has been selected but not confirmed
                job: null,
                // if they have clicked conduct asbestos assessment
                hasAesbestosRisk: false
            };

            // whether we're in the edit mode for the job

            clientDefaults.editJob = !oh.soc_job;

            var existingClient = oh._client || {};

            var result = _.extend(clientDefaults, existingClient);
            result.aes.asbestos_exposure_screening.related_occupation_id = result.id;
            return result;
        };

        scope.select = function(job, occupational_history){
            occupational_history._client.job = job;
        };

        scope.filterChanged = function(client){
            return SocCodeService.search(client.soc_job_filter).then(function(matches){
              client.matches = matches;
            })
        };

        scope.hasAEH = function(oh){
          return oh._client.hasAesbestosRisk;
        };

        scope.confirm = function(oh){
            _.each(oh, function(v, k){
              if(k !== "_client"){
                oh[k] = undefined;
              }
            });
            oh._client.aeh = [];
            oh.soc_code_id = oh._client.job.id;
            if(scope.socCodes[oh.soc_job]){
              scope.addAnotherAEH(oh._client.aeh, oh);
            }
            oh._client.soc_job_filter = null;
            oh._client.editJob = false;
        };

        scope.get_soc_details = function(client){
            if(client.job){
                return '/soc/details/?title=' + client.job.title;
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

        scope.cancelAesbestosRisk = function(oh){
          oh._client.hasAesbestosRisk = false;
          oh._client.aeh = [];
          oh._client.aes = {
            asbestos_exposure_screening: {
              _client: _.uniqueId("asbestos_screening"),
              related_occupation_id: oh._client.id
            }
          };
        };

        scope.addAnotherAEH = function(asbestos_exposure_history, oh){
          oh._client.hasAesbestosRisk = true;
          var c = {asbestos_exposure_history: {
            _client: {completed: false, id: _.uniqueId("asbestos_exposure_history")},
            related_occupation_id: oh._client.id
          }};

          asbestos_exposure_history.push(c);
        };

        scope.removeAEH = function(occupational_history, index){
          occupational_history._client.aeh.splice(index, 1);
        };


        scope.socCodes = {};
        scope.aspestos_risk = {};

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

                    if(oh.soc_code_id){
                      SocCodeService.load(oh.soc_code_id).then(function(job){
                        oh._client.job = job;
                        oh._client.soc_job_filter = job.title;
                      })
                    }

                    var nestedAeh = [];

                    if(oh.id){
                        nestedAeh = _.where(scope.editing.asbestos_exposure_history, {related_occupation_id: oh.id});

                        scope.editing.asbestos_exposure_history = _.filter(scope.editing.asbestos_exposure_history, function(aeh){
                            return aeh.related_occupation_id !== oh.id;
                        });

                        _.each(nestedAeh, function(aeh){
                            aeh.related_occupation_id = oh._client.id;
                        });

                        _.each(nestedAeh, function(aeh){
                          oh._client.aeh.push({asbestos_exposure_history: aeh});
                        });

                        var nestedAes = _.where(scope.editing.asbestos_exposure_screening, {related_occupation_id: oh.id});
                        if(nestedAes.length){
                          oh._client.aes.asbestos_exposure_screening = nestedAes[0];
                          scope.editing.asbestos_exposure_screening = _.filter(scope.editing.asbestos_exposure_screening, function(aes){
                              return aes.related_occupation_id !== oh.id;
                          });
                          oh._client.aes.asbestos_exposure_screening.related_occupation_id = oh._client.id;
                        }

                        if(nestedAeh.length | oh._client.aes.asbestos_exposure_screening.id){
                          oh._client.hasAesbestosRisk = true;
                        }
                    }
                });
            }
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
                if(scope.hasAEH(oh)){
                  _.each(oh._client.aeh, function(aeh){
                    editing.asbestos_exposure_history.push(aeh.asbestos_exposure_history);
                  });
                  if(!editing.asbestos_exposure_screening){
                    editing.asbestos_exposure_screening = [];
                  }
                  else if(!_.isArray(editing.asbestos_exposure_screening)){
                    editing.asbestos_exposure_screening = [
                      editing.asbestos_exposure_screening
                    ];
                  }
                  editing.asbestos_exposure_screening.push(
                    oh._client.aes.asbestos_exposure_screening
                  );
                }
            });
        };

        scope.initialise();
    });
