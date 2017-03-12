/*global app*/
app.controller('MainController', ['$scope', 'company_profile', function ($scope, company_profile) {
    company_profile.success(function (data) {
        $scope.metrics = data;
    });
}]);