import logging
from conf.settings import LOG_DIR
from threading import Thread,Semaphore
from core.handler import 通信循环
import socket

logger = logging.getLogger("logger_both")



def main(ip,端口,连接数):
    sp=Semaphore(连接数)
    连接_套接字=socket.socket()
    连接_套接字.bind((ip,端口))
    连接_套接字.listen(128)
    logger.info(f"日志写入：{LOG_DIR}")
    while True:
        客户_套接字,客户_信息=连接_套接字.accept()
        客户_套接字.settimeout(10)#一句话给加下来所有recv加上限时,防止客户抢占位置
        logger.warning(f"一位客户连接{客户_信息}")
        sp.acquire()
        p=Thread(target=通信循环,args=(客户_套接字,sp,客户_信息)).start()




        
