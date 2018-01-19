angular.module('opal.services').factory('SocCodeService', function($http, $q, $window){
  var load = function(id){
    var deferred = $q.defer();
    var url = '/ipfjes_api/v0.1/soc_code_list/' + id + "/";
    $http({ cache: true, url: url, method: 'GET'}).then(function(response) {
        deferred.resolve(response.data);
    }, function() {
      // handle error better
      $window.alert('SocCode could not be loaded');
    });

    return deferred.promise;
  };

  var search = function(someStr){
    var url = '/ipfjes_api/v0.1/soc_code_list/?search=' + someStr;
    var deferred = $q.defer();

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
    load: load,
    search: search
  };
});
