import socket

HOST = ''
PORT = 2016

def main():
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    scope_id = socket.if_nametoindex('lowpan0')
    s.bind((HOST, PORT, 0, scope_id))
    s.listen(1)

    count = 1
    while True:
        conn, addr = s.accept()
        conn.send(b'123ABC')
        conn.close()

if __name__ == '__main__':
    main()
