import logging
logger = logging.getLogger("logger_both")



def 通信循环(客户_套接字,sp,客户_信息):
    while True:
        try:
            数据_字节=客户_套接字.recv(1024)
            if not 数据_字节:
                logger.warning(f"用户断开连接{客户_信息}")
                break
            客户_套接字.send(数据_字节.upper())
            if 数据_字节.decode("utf-8") == "dsh":
                logger.warning(f"用户断开连接{客户_信息}")
                break
        except Exception as e: 
            logger.warning(f"连接异常 {客户_信息}: {e}")
            break
    客户_套接字.close()
    sp.release()