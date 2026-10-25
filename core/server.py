import logging
from conf.settings import LOG_DIR
from threading import Thread,Semaphore
from core.handler import 通信循环
import socket

logger = logging.getLogger("logger_both")



def main(ip,端口,连接数):
    client_sum=0
    sp=Semaphore(连接数)
    连接_套接字=socket.socket()
    连接_套接字.bind((ip,端口))
    连接_套接字.listen(128)
    logger.info(f"日志写入：{LOG_DIR}")
    客户_套接字 = None 
    try:
        while True:
            客户_套接字,客户_信息=连接_套接字.accept()
            client_sum+=1
            客户_套接字.settimeout(10)#一句话给加下来所有recv加上限时,防止客户抢占位置
            logger.warning(f"一位客户连接{客户_信息}")
            sp.acquire()
            p=Thread(target=通信循环,args=(客户_套接字,sp,客户_信息)).start()
    except KeyboardInterrupt:
        logger.warning(f"收到了 Ctrl+C,准备停止")
    finally:
        logger.warning(f"共处理{client_sum}个连接")
        if 客户_套接字:
            客户_套接字.close()
            连接_套接字.close()




        
