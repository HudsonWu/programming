1. Download Composer
```
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php --install-dir=/usr/bin/ --filename=composer
php -r "unlink('composer-setup.php');"
composer config -g repo.packagist composer https://packagist.phpcomposer.com  // Chinese mirror
```

2. Create laravel project
```
composer create-project laravel/laravel --prefer-dist  //install laravel in the current directory
php artisan serve  //start the laravel service
```

3. Application Structure of Laravel
```
 1) Root Directory
app/  This directory contains the core code of the application
bootstrap/  This directory contains the application bootstrapping script
config/  This directory contains configuration files of application
database/  This folder contains your database migration and seeds
public/  This is the application's document root. It starts the Laravel application. It also contains the assets of the application like Javascript, CSS, Images, etc
resources/  This directory contains raw assets such as the LESS & Sass file, localization and lanuage files, and Templates that are rendered as HTML
storage/  This directory contains App storage, like file uploads etc. Framework storage(cache), and application-generated logs
test/  This directory contains various test cases
vendor/  This directory contains composer dependencies
 2) App Directory
Console/  All the artisan commands are stored in this directory
Events/  This directory stores events that your application can raise. Events may be used to alert other parts of your application that given action has occurred, providing a great deal of flexibility and decoupling
Exceptions/  This directory contains your application's exception handler and is also a good place to stick any exceptions thrown by your application
Http/  This directory contains your controllers, filters, and requests
Jobs/  This directory contains the queueable jobs for your application
Listeners/  This directory contains the handler classes for your events. Handlers receive an event and perform logic in response to the event being fired. For example, a UserRegisterd event might be handled by a SendWelcomeEmail listener
Policies/  This directory contains various policies of the application
Providers/  This directory contains various service providers
```

4. Configuration
```
 1) Set the write permission for the directory storage and bootstrap/cache
 2) Generate Application key to secure session and other encrypted data. Make sure the root directory contains the .env file, then execute the command: "php artisan key:generate"
 3) You can also configure the locale, time zone, etc. of the application in the config/app.php file
 4) Environmental Configuration
Laravel provides facility to run your application in different environment like testing, production etc. You can configure the environment of your application in the .env file of the root directory of your application
APP_ENV  local, production, testing
 5) Database Configuration
config/database.php
```

5. Naming the application
```
The App directory, by default, is namespaced under App. To rename it, you can execute the command: "php artisan app:name newname"
```

6. Maintenance Mode
```
start maintenance mode: "php artisan down"
stop maintenance mode: "php artisan up"
```
