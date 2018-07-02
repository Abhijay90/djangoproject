var app = app || angular.module("blog", []);

app.controller("list_blog",function($scope,asynNetworkService) {
	var urls = [
    { 'key': 'blog_list', 'url': '/list_view' },
	];

	$scope.blog_list

	$scope.postInit=function(result){
		if(result["blog_list"]["status"]){
			$scope.blog_list=result["blog_list"]["data"];
		}
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
	window.debug=$scope;

	console.log("add-blog");
	var urls ={ 'key': 'blog_list', 'url': '/add_blog_api' };

	$scope.text_input="";



	$scope.postdata=function(){
		// console.log($scope.blog_name);
		// console.log($scope.blog_data);

		if ($scope.blog_name && $scope.blog_data){
			data = {"title":$scope.blog_name , "content":$scope.blog_data}
			asynNetworkService.post(urls.url,data).then(function(result) {
				console.log(result);
			});
		}
	}

	// $scope.init();

}

);

app.controller("view_blog",function($scope,asynNetworkService) {
	window.debug=$scope;

	var blog_id = window.location.pathname.split('/')[2];

	var urls = [
    { 'key': 'blog_data', 'url': '/view_blog_api/'+blog_id },
	];
	console.log(urls)
	
	$scope.postInit=function(result){
			console.log();
			
			if (result.blog_data.status){
				$scope.title=result.blog_data.title;
				$scope.paragraph=result.blog_data.paragraph;
				$scope.show_comment(result.blog_data.paragraph[0].id);
			}
		}

	$scope.init=function(){
		asynNetworkService.get(urls).then(function(result) {
                $scope.postInit(result);
            }, function(error) {
                console.log("error loading data..check network services."); 
            });
    
	}

	$scope.init();


	$scope.get_comment=function(id){
		$scope.show_error=false;
		$scope.showaddComment=false;
		var comment_urls = [
	    { 'key': 'comment', 'url': '/view_comment_api/'+id },
		];

		asynNetworkService.get(comment_urls).then(function(result) {
			$scope.comment_list=[]
			if (result.comment.status){
				$scope.comment_list = result.comment.comment_list;
			}


		});
	}

	$scope.show_comment=function(paragraph_id){
		$scope.active_para=paragraph_id;
		$scope.get_comment(paragraph_id);
	}


	$scope.addComment=function(comment){
		$scope.postComment($scope.active_para,comment);

	}

	$scope.postComment=function(paragraph_id,comment){
		var comment_urls = { 'key': 'comment', 'url': '/view_comment_api/'+paragraph_id+"/" };
		data={"content":comment,"paragraph_id":paragraph_id};
		console.log(comment_urls);
		console.log(data);
		asynNetworkService.post(comment_urls.url,data).then(function(result) {
				if (result.status){
					$scope.show_comment($scope.active_para);
				}
				else{
					console.log("why");
					$scope.show_error=true;
				}
			});
	}

}

);