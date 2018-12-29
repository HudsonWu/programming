# middleware

Middleware acts as a middle man between request and response. It is a type of filtering mechanism.

For example, Laravel includes a middleware that verifies whether user of the application is authenticated or not. If the user is authenticated, he will be redirected to the home page otherwise, he will be redirected to the login page

## Register Middleware

### We need to register each and every middleware before using it. There are two types of Middleware in Laravel:

```
Global Middleware
Route Middleware
```

### The middleware can be registered at app/Http/Kernel.php, this file contains two properties $middleware and $routeMiddleware

1. To create middleware: " php artisan make:middleware RoleMiddleware "
2. The middleware that you create can be seen at app/Http/Middleware directory
3. Add the following code  in the handle method of RoleMiddleware.php
```
<?php
namespace App\Http\Middleware;
use Closure;

class AgeMiddleware {
    public function handle($request, Closure $next, $role) {
        echo "Role: ".$role;
        return $next($request);
    }
}
```
4. Register the middleware (app/Http/Kernel.php)
```
<?php
namespace App\Http;
use Illuminate\Foundation\Http\Kernel as HttpKernel;

class Kernel extends HttpKernel {
    protected $middleware = [
        \Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode::class,
        \App\Http\Middleware\EncryptCookies::class,
        ...
    ];

    protected $routeMiddleware = [
        'auth' => \App\Http\Middleware\Authenticate::class,
        ...
        'Role' => \App\Http\Middleware\RoleMiddleware::class,
    ];
}
```
5. To create TestController: " php artisan make:controller TestController --plain "
6. app/Http/TestController.php
```
<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Http\Requests;
use App\Http\Controllers\Controller;

class TestController extends Controller {
    public function index() {
        echo "<br>Test Controller.";
    }
}
```
7. Add the following line of code in app/Http/routes.php file
```
Route::get('role', [
    'middleware' => 'Role:editor',
    'users' => 'TestController@index',
]);
```
8. http://localhost:8000/role
```
Role:editor
Test Controller.
```
