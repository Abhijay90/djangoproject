var app = app || angular.module("blog", []);

app.controller("list_blog",function($scope,asynNetworkService) {
	var urls = [
    { 'key': 'blog_list', 'url': '/list_view' },
	];

	$scope.postInit=function(result){
		console.log(result);
	}

	$scope.init=function(){
		asynNetworkService.get(urls).then(function(result) {
                $scope.postInit(result);
            }, function(error) {
                console.log("error loading data..check network services."); 
            });
    
	}

	$scope.init();

}
);

app.controller("add_blog",function($scope,asynNetworkService) {

var urls = [
    { 'key': 'blog_list', 'url': '/list_view' },
	];

	$scope.postInit=function(result){
		console.log(result);
	}

	$scope.init=function(){
		asynNetworkService.get(urls).then(function(result) {
                $scope.postInit(result);
            }, function(error) {
                console.log("error loading data..check network services."); 
            });
    
	}

	$scope.init();

}

});

app.controller("view_blog",function($scope,asynNetworkService) {

var urls = [
    { 'key': 'blog_list', 'url': '/list_view' },
	];

	$scope.postInit=function(result){
		console.log(result);
	}

	$scope.init=function(){
		asynNetworkService.get(urls).then(function(result) {
                $scope.postInit(result);
            }, function(error) {
                console.log("error loading data..check network services."); 
            });
    
	}

	$scope.init();

}

});