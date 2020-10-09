import socket
import time

ADDR = '2001:db8::1'
PORT = 2016

def main():
    scope_id = socket.if_nametoindex('lowpan0')
    while True:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        s.connect((ADDR, PORT, 0, scope_id))
        data = s.recv(1024)
        print(data.decode('ascii'), end='')
        time.sleep(10)

if __name__ == '__main__':
    main()
