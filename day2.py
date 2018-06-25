import socket,gevent
from gevent import socket,monkey
from gevent.pool import Pool
monkey.patch_all()
HOST = '127.0.0.1'
PORT = 8888
def sockclient(i):
    s = socket.socket()
    s.connect((HOST,PORT))
    print(gevent.getcurrent())
    msg = bytes('This is gevent:%s'%i,encoding='utf-8')
    s.sendall(msg)
    data = s.recv(1024)
    print('Received:',data.decode())
    s.close()
pool = Pool(5)
threads = [pool.spawn(sockclient,i) for i in range(2000)]
gevent.joinall(threads)