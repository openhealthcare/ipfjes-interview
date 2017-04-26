angular.module('opal.services').factory('SocCodeService', function($http, $q, $window){
  var url = '/ipfjes_api/v0.1/soc_code_at_risk/';
  var load = function(){
    var deferred = $q.defer();
    $http({ cache: true, url: url, method: 'GET'}).then(function(response) {
        deferred.resolve(response.data);
    }, function() {
      // handle error better
      $window.alert('SocCode could not be loaded');
    });

    return deferred.promise;
  };

  return {
    load: load
  };
});
