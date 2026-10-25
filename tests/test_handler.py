
import socket

from core.handler import 通信循环
class FakeSocket:
    """假类,包含着假方法"""
    def __init__(self,incoming:list[bytes], raise_timeout=False):
        """基本信息"""
        self.raise_timeout = raise_timeout
        self.incoming=incoming
        self.sent = []#存储发出去的信息
        self.closed = False#默认没关,检查代码会不会关
        
    def recv(self,n):
        """假接受,且模仿关闭"""
        if self.raise_timeout:
            raise socket.timeout("timed out")
        if not self.incoming:
            return b""
        data=self.incoming.pop(0)
        return data
    
    def send(self,data):
        """假发送,并记录"""
        self.sent.append(data)
        
    def close(self):
        self.closed = True

class FakeSemaphore:
    """假报错,检查服务端是否捕获了报错"""
    def __init__(self):
        self.released = 0
    def release(self):
        """假锁,看看有没有真的释放"""
        self.released += 1
    


def test_正常echo():
    fake_sp = FakeSemaphore()
    fake_so = FakeSocket([b"abc", b"dsh"])

    通信循环(fake_so, fake_sp, ("127.0.0.1", 1234))   # ← 就这一行，直接传

    assert fake_so.sent[0] == b"ABC"
    assert fake_so.closed is True
    assert fake_sp.released == 1
    
def test_客户端关闭():
    fake_sp=FakeSemaphore()
    fake_so=FakeSocket(incoming=[b""])
    通信循环(fake_so, fake_sp, ("127.0.0.1", 1234))
    assert fake_so.closed is True
    assert fake_sp.released == 1
    
def test_超时捕捉():
    fake_sp=FakeSemaphore()
    fake_so=FakeSocket(incoming=[b""])
    通信循环(fake_so, fake_sp, ("127.0.0.1", 1234))
    assert fake_so.closed is True
    assert fake_sp.released == 1


    
    