var app = app || angular.module("blog", []);


app.service(
    "asynNetworkService",
    function($http, $q) {
        return ({
            get: get,
            post: post,
        });

        // ---
        // PUBLIC METHODS.
        // ---

        function get(urls) {
            var resp = {};
            var deferred = $q.defer();
            var urlCalls = [];
            urls = angular.isArray(urls) ? urls : [{'url':urls, 'key':'default'}];

            angular.forEach(urls, function(url) {
                urlCalls.push(
                    $http({
                        method: "get",
                        url: url.url,
                        params: url.params || {},
                    })
                );
            });

            $q.all(urlCalls)
                .then(
                function(results) {
                    var resp = {};
                    angular.forEach(urls, function(v, i){
                        resp[v.key] = results[i].data;
                    });
                    /*deferred.resolve(
                        JSON.stringify(results))*/
                    deferred.resolve(resp)
                },
                function(errors) {
                    deferred.reject(errors);
                    console.warn( errors.config.url, errors.status, errors.statusText );
                },
                function(updates) {
                    angular.forEach(urls, function(v, i){
                        resp[v.key] = updates[i].data;
                    });
                    deferred.update(resp);
            });
            return deferred.promise;

        }

        function post(url,data) {
            var resp = {};
            var deferred = $q.defer();
            var request = $http({
                method: "post",
                url: url,
                data: data
            });
            request.then(
                function(results) {
                    /*deferred.resolve(
                        JSON.stringify(results)) */
                    resp = results.data;
                    deferred.resolve(resp);
                },
                function(errors) {
                    deferred.reject(errors);
                },
                function(updates) {
                    resp = updates.data;
                    deferred.update(resp);
            });

            return deferred.promise;
        }

    }
);
