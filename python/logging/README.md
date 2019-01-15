# Logging in Python

## The level of severity

+ DEBUG
+ INFO
+ WARNING
+ ERROR
+ CRITICAL

## Basic Configurations

Some of the commonly used parameters for `basicConfig()`:
+ level: The root logger will be set to the specified severity level
+ filename: Specifies the file
+ filemode: If `filename` is given, the file is opened in this mode, default is `a`
+ format: The format of the log message

1. Set what level of log messages

```console
> import logging

> logging.basicConfig(level=logging.DEBUG)
> logging.debug('This will get logged')
DEBUG:root:This will get logged
```

2. Written to a file

```console
> import logging

> logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
> logging.warning('This will get logged to a file')
root - ERROR - This will get logged to a file
```

3. Formatting the Output

```console
> import logging

> logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
> logging.warning('This is a Warning')
18472-WARNING-This is a Warning
```

```console
> import logging

> logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
> logging.info('Admin logged in')
2018-07-11 20:12:06,288 - Admin logged in
```

## Capturing Stack Traces

```python
import logging

a = 5
b = 0

try:
  c = a / b
  except Exception as e:
    logging.error("Exception occurred", exc_info=True)
```

```python
import logging

a = 5
b = 0
try:
  c = a / b
  except Exception as e:
    logging.exception("Exception occurred")
```
Using `logging.exception()` would show a log at the level of ERROR. If you don’t want that, you can call any of the other logging methods from `debug()` to `critical()` and pass the `exc_info` parameter as True.

## Classes and Functions

You can (and should) define your own logger by creating an object of the Logger class, especially if your application has multiple modules. 

The most commonly used classes defined in the logging module are the following
+ Logger: This is the class whose objects will be used in the application code directly to call the functions.
+ LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.
+ Handler: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.
+ Formatter: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

```python
# logging_example.py

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```

output:
```
__main__ - WARNING - This is a warning
__main__ - ERROR - This is an error
```

Here, logger.warning() is creating a LogRecord that holds all the information of the event and passing it to all the Handlers that it has: `c_handler` and `f_handler`.

`c_handler` is a StreamHandler with level WARNING and takes the info from the LogRecord to generate an output in the format specified and prints it to the console. `f_handler` is a FileHandler with level ERROR, and it ignores this LogRecord as its level is WARNING.

When logger.error() is called, `c_handler` behaves exactly as before, and `f_handler` gets a LogRecord at the level of ERROR, so it proceeds to generate an output just like `c_handler`, but instead of printing it to console, it writes it to the specified file in this format:

```
2018-08-03 16:12:21,723 - __main__ - ERROR - This is an error
```

## Other Configuration Methods

You can configure logging as shown above using the module and class functions or by creating a config file or a dictionary and loading it using `fileConfig()` or `dictConfig()` respectively. These are useful in case you want to change your logging configuration in a running application.

Here's an example file configuration:
```
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)
```

In the above file, there are two loggers, one handler, and one formatter. After their names are defined, they are configured by adding the words logger, handler, and formatter before their names separated by an underscore.

To load this config file, you have to use `fileConfig()`:

```python
import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```

The path of the config file is passed as a parameter to the `fileConfig()` method, and the `disable_existing`_loggers parameter is used to keep or disable the loggers that are present when the function is called. It defaults to True if not mentioned.

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  sampleLogger:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

```python
import logging
import logging.config
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
```
