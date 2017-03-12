/*global app*/
app.controller('MainController', ['$scope', '$http', function ($scope, $http) {
    $scope.method = 'GET';
    $scope.text = 'hello';
    $scope.url = 'localhost:8000/hi';
    $scope.submit = function() {
        $scope.code = null;
        $scope.response = null;
        $http({method: $scope.method, url: $scope.url}).
        then(function(response) {
          $scope.status = response.status;
          $scope.data = response.data;
        }, function(response) {
          $scope.data = response.data || 'Request failed';
          $scope.status = response.status;
      });
    };
}]);