angular.module('opal.controllers').controller(
    'OccupationalHistoryCtrl',
    function($http, scope, step, episode, Referencedata){
        "use strict"
        Referencedata.then(function(referencedata){
            scope.referencedata = referencedata;

            scope.matches = []
            scope.query = {}

            scope.$watch('query.soc_job_filter', function(){
                if(!scope.query.soc_job_filter){ return }
                if(scope.query.soc_job_filter.length < 3){
                    return
                }
                scope.matches = _.filter(scope.referencedata.socjob, function(j){
                    return j.toLowerCase().indexOf(scope.query.soc_job_filter.toLowerCase()) != -1;
                })
            })

            scope.select = function(what){
                scope.selected = what
            }

            scope.get_soc_details = function(){
                return '/soc/details/?title=' + scope.selected;
            };



        })

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
