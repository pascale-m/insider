/*global app*/
app.controller('MainController', ['$scope', 'company_data', function ($scope, company_data) {
    forecast.company_data(function (data) {
        $scope.company_data = data;
    });
}]);