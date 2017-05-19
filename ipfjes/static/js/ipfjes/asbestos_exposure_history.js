angular.module('opal.controllers').controller('AsbestosExposureHistoryCtrl', function(scope, step, episode){
    "use strict";
    if(scope.editing.asbestos_exposure_screening.length){
      scope.editing.asbestos_exposure_screening = _.first(scope.editing.asbestos_exposure_screening);
    }
});
