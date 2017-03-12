/*global app*/
app.factory('company_profile', ['$http', function ($http) {
    return $http.get('http://api.apixu.com/v1/forecast.json?key=b4572c56d52945ca88841916172002&q=v8t3w4&days=5')
        .success(function (data) {
            return data;
        })
        .error(function (err) {
            return err;
        });
}]);