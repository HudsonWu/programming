# Publish/Subscribe

+ 接收并保存'warning'、'error'日志信息到文件中：`./receive_logs_direct.py warning error > logs_from_rabbit.log`
+ 接收并打印所有日志到屏幕中：`./receive_logs_direct.py info warning error`
+ 发送日志消息：`./emit_log_direct.py error "Run. Run. Or it will explode."`
