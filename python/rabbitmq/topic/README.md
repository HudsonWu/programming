# Publish/Subscribe

+ 接收并打印所有日志消息：`./receive_logs_topic.py "#"`
+ 接收并打印所有kern日志消息：`./receive_logs_topic.py "kern.*"`
+ 接收并打印所有critical的日志消息：`./receive_logs_topic.py "*.critical"`
+ 接收并打印所有kern或者critical的日志消息：`./receive_logs_topic.py "kern.*" "*.critical"`
+ 发送`routing_key`为`kern.critical`的消息：`./emit_log_topic.py "kern.critical" "A critical kernel error"`

