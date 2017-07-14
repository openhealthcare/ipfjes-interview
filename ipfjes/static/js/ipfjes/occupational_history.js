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

        scope.hasAEH = function(oh){
          return oh._client.hasAesbestosRisk;
        };

        scope.confirm = function(oh){
            oh._client.aeh = [];
            oh.soc_job = oh._client.job || oh._client.soc_job_filter;
            if(scope.socCodes[oh.soc_job]){
              scope.addAnotherAEH(oh._client.aeh, oh);
            }
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
