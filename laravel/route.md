## Basic Routing

Basic routing is meant to route your request to an appropriate controller. The routes of the application can be defined in app/Http/routes.php file. Here is the general route syntax for each of the possible request
```
Route::get('/', function () {
    return 'Hello World'
});

Route::post('foo/bar', function () {
    return 'Hello World'    
});

Route::put('foo/bar', function () {
    //
});

Route::delete('foo/bar', function () {
    //
});
```

### Example

app/Http/routes.php
```
<?php
Route::get('/', function () {
    return view('welcome');    
});
```

resources/view/welcome.blade.php
```
<!DOCTYPE html>
<html>
    <head>
        <title>Laravel</title>
        <link href = "https://fonts.googleapis.com/css?family=Lato:100" rel = "stylesheet" type = "text/css">
        <style>
            html, body {
                height: 100%    
            }
            body {
                margin: 0;
                padding: 0;
                width: 100%;
                display: table;
                font-weight: 100;
                font-family: 'Lato';
            }
            .container {
                text-align: center;
                display: table-cell;
                vertical-align: middle;
            }
            .content {
                text-align: center;
                display: inline-block;
            }
            .title {
                font-size: 96px;
            }
        </style>
    </head>
    <body>
        <div class = "container">
            <div class = "content">
                <div class = "title">Laravel 5</div>
            </div>
        </div>
    </body>
</html>
```

Let us now understand the steps in detail:
1. we need to execute the root URL of the application
2. the executed URL will match with the appropriate method in the route.php file. In our case, it will match to get the method and the root('/')URL. This will execute the related function
3. the function calls the template file resources/views/welcome.blade.php. the function later calls the view() function with argument 'welcome' without using the blade.php.

## Routing Parameters

Required Parameters (http://localhost:8000/ID/5)
```
Route::get('ID/{id}', function($id){
    echo 'ID: '.$id;
});
```

Optional Parameters (http://localhost:8000/user/Virat)
```
Route::get('/user/{name?}', function($name = 'Virat'){
    echo "Name: ".$name;
});
```
