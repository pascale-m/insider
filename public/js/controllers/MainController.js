/*global app*/
app.controller('MainController', ['$scope', '$http', function ($scope, $http) {
    $scope.method = 'GET';
		$scope.testnum = 22;
    $scope.submit = function() {
        $scope.code = null;
        $scope.response = null;
				$scope.url = 'http://localhost:5000/'+$scope.text;
        $http({method: $scope.method, url: $scope.url}).
        success(function successfulResponse(response) {
          $scope.status = response.status;
          $scope.data = JSON.parse(response.data);
        }, function errorResponse(response) {
          $scope.data = response.data || 'Request failed';
          $scope.status = response.status;
          console.log('failure :(')
      });
    };
}]);