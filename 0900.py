#!/usr/bin/env python

import socket
import time

addr=('127.0.0.1',8000)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建sock的对象
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(addr)  # 绑定服务器地址
sock.listen(100) # 设置监听队列

# 等待接受客户端连接
# 第一个返回值是客户端的 socket 对象
# 第二个返回值是客户端的地址
# cli_sock,cli_addr= sock.accept()
#
# cli_data=cli_sock.recv(1024)  # 接受客户端传来的数据，1024是接受缓冲区的大小

#  定义“响应报文”
html=b'''

    HTTP/1.1 200 OK
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        HELLO WORLD
    
    </body>
</html>
'''
while True:
    print('服务器一运行，正在等待客户端链接')
    cli_sock,cli_addr=sock.accept()
    cli_data=cli_sock.recv(1024)

# 向客户端发送数据
cli_sock.sendall(b'html')
# 断开与客户端的连接
cli_sock.close()
