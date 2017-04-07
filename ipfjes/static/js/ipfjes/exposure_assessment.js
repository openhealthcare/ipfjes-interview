angular.module('opal.controllers').controller(
    'ExposureAssessmentCtrl',
    function($http, scope, step, episode){
        "use strict"

        scope.editing = {};

        var handling_tasks = {

        }

        var emission = {
            'Amosite'    : {'100%': 5, '20-40%'  : 4, '10-15%': 1.2, '1%': 0.4},
            'Crocidolite': {'100%': 5, '20-40%'  : 4, '10-15%': 1.2, '1%': 0.4},
            'Chrysotile' : {'100%': 2.5, '20-40%': 2, '10-15%': 0.6, '1%': 0.2}
        };

        var calculate_risks = function(){
            if(scope.editing.type){
                if(scope.editing.per_asbestos){
                    scope.intrinsic_emission = emission[scope.editing.type][scope.editing.per_asbestos];
                }
            }

            var intrinsic = scope.editing.intrinsic_emission || scope.intrinsic_emission
            scope.active_emission = parseFloat(intrinsic) * parseFloat(scope.editing.handling) * parseInt(scope.editing.local_controls);

            var active_emission = scope.active_emission
            if(scope.editing.active_emission){
                var active_emission = scope.editing.active_emission
            }

            scope.total_emission = active_emission + parseFloat(scope.editing.passive);
            scope.fractional_exposure = scope.total_emission * parseFloat(scope.editing.time_active) * parseFloat(scope.editing.general_ventilation) * parseFloat(scope.editing.ppe) * (parseFloat(scope.editing.time_on_task)/100);
        };

        scope.$watch('editing', function(newval, oldval){
            calculate_risks()
        }, true);
    });
