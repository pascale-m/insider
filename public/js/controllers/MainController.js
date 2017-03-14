/*global app*/
app.controller('MainController', ['$scope', '$http', function ($scope, $http) {
    $scope.method = 'GET';
    $scope.url = 'http://localhost:5000/hi';
    $scope.submit = function() {
        $scope.code = null;
        $scope.response = null;
        $http({method: $scope.method, url: $scope.url}).
        success(function successfulResponse(response) {
          $scope.status = response.status;
          $scope.data = response.data;
          console.log(response.data+' '+response.status);
        }, function errorResponse(response) {
          $scope.data = response.data || 'Request failed';
          $scope.status = response.status;
          console.log('failure :(')
      });
    };
}]);