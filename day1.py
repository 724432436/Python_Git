import sys,socket,time
from gevent import socket,monkey,pool
monkey.patch_all()
def server(port,pool):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen()
    while True:
        cli,addr = s.accept()
        print('Wellcom %s to SockerServer' %str(addr[0]))
        pool.spawn(handle_request,cli)
def handle_request(conn):
    try:
        data = conn.recv(1024)
        print('recv:%s'%data)
        data ='From sockServer :127.0.0.1--->%s'%data.decode('utf-8')
        conn.sendall(bytes(data,encoding='utf-8'))
        if not data:
            conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
if __name__ == '__main__':
    pool = pool.Pool(5)
    server(8888,pool)