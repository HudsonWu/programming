# Work queues, 工作队列

创建一个工作队列，用于在多个worker之间分配耗时的任务。主要思想是在遇到资源密集型任务时，避免立即执行而且必须等待它完成的做法，而是把任务安排到之后完成。我们将任务封装为消息并将其发送到队列，一个后台的工作进程(worker)接收到任务并最终完成job，当有多个worker时，任务将在它们之间共享。


