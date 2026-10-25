信号量 TCP 服务端



是什么

一句话：TCP echo 服务器，把客户端发来的数据转成大写发回；用信号量限制最大并发连接数。



怎么运行

python bin/run.py



怎么配置

conf/settings.py —— 改 ip / 端口 / 最大连接数 / 日志级别



怎么测

python -m pytest



已知限制

\- 单机、纯文本协议，无 TLS

\- 客户端 10 秒不说话会被断开

\- 最大并发连接数靠信号量控制（默认 1）

\- 没有做粘包处理（每次 recv 1024 字节）



项目结构

bin/run.py      入口

core/server.py  监听 / accept / 信号量

core/handler.py 单连接处理

conf/settings.py 配置

tests/          单元测试

