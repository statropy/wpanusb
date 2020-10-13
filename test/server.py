import socket

HOST = ''
PORT = 2018

def main():
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0) as s:
        scope_id = socket.if_nametoindex('lowpan0')
        s.bind((HOST, PORT, 0, scope_id))
        s.listen(1)
        print("Listening on port", repr(PORT))

        while True:
            conn, addr = s.accept()
#            try:
            print("Connection:", repr(addr))
            while True:
                 data = conn.recv(1)
                 #print('received', str(len(data)))
                 if data:
                     conn.send(data)
                 else:
                     print('end')
                     conn.close()
                     break

if __name__ == '__main__':
    main()
