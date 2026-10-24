import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logging.config
from conf.settings import LOG_CONFIG
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger("logger_both")

from threading import Thread,Semaphore
from core.handler import 通信循环
import socket



def main(ip,端口,连接数):
    sp=Semaphore(连接数)
    连接_套接字=socket.socket()
    连接_套接字.bind((ip,端口))
    连接_套接字.listen(128)
    while True:
        客户_套接字,客户_信息=连接_套接字.accept()
        logger.info(f"日志写入：{LOG_CONFIG["handlers"]["file_handler"]["filename"]}")
        logger.warning(f"一位客户连接{客户_信息}")
        sp.acquire()
        p=Thread(target=通信循环,args=(客户_套接字,sp,客户_信息)).start()




        
